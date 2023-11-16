import time, json
import urllib.request as curl
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from tresult import TestResult

def ajax(paragraph, driver):
    url = urljoin(driver.current_url, f'/text/data?paragraph={paragraph}')
    page = curl.urlopen(url)
    print("page", page)
    return json.loads(page.read())

def check_paragraph(driver, para, expected, res):
    n = para['paragraph']
    if int(n) != expected:
        res.fail(f'Q3 All, Paragraph {n}',
                 "Bug: mismatching paragraph number. Please talk to instructor")
        return False
    paragraph_id = f"paragraph_{n}"
    elems = driver.find_elements(by='id', value=paragraph_id)
    num_elems = len(elems)
    if len(elems) != 1:
        res.fail(f'Q3 All, Paragraph {n}',
                 f'Found {num_elems} elements with id={paragraph_id}. Expect 1')
        return False
    elem = elems[0]
    if para['content'] not in elem.text:
        res.fail(f'Q3 All, Paragraph {n}',
                 f"Cannot find matching paragraph content, expecting '{para['content']}'")
        return False
    return True

def check_page(driver, data, page, res):
    pn = page * 5 + 1
    for para in data:
        if check_paragraph(driver, para, pn, res) is False:
            return False
        pn += 1
    res.succeed(f'Q3 All, Page {page}')
    return True

def test_all_pages(driver):
    res = TestResult()
    page = 0

    while True:
        resp = ajax(page * 5 + 1, driver)
        check_page(driver, resp['data'], page, res)
        page += 1

        # stop looking for paragraph
        if resp['next'] is False:
            break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)


    return res