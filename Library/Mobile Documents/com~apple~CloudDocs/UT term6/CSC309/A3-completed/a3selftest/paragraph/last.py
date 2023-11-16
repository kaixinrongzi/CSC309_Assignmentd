from tresult import TestResult
from selenium.webdriver.common.keys import Keys
import time

def test_no_more_pages(driver):
    res = TestResult()

    paragraph = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    failed = False
    while True:
        # there are 27 paragraphs
        if paragraph > 27:
            res.fail('Q3 No More Page', 
                     'No more request should be sent after the last page is fetched.')
            failed = True
            break
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        paragraph += 5
        if new_height == last_height:
            break
        last_height = new_height
        
    if paragraph < 27:
        res.fail('Q3 No More Page', 
                 'Not all paragraphs have been fetched.')
    elif not failed:
        res.succeed('Q3 No More Page')

    html = driver.find_element(by='tag name', value='html')
    html.click()
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)

    if html.text.lower().count("you have reached the end") == 0:
        res.fail('Q3 No More Page', '"You have reached the end" is not in the page.')
    elif html.text.lower().count("you have reached the end") > 1:
        res.fail('Q3 No More Page', 'At least 2 "You have reached the end" are found in the page.')
    else:
        res.succeed('Q3 No More Page')
    return res