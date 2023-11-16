import time
from tresult import TestResult

def test_decrease_increase(driver):
    res = TestResult()

    # Setup
    name = driver.find_element(by='id', value='name')
    price = driver.find_element(by='id', value='price')
    quantity = driver.find_element(by='id', value='quantity')
    add_update_item_button = driver.find_element(by='id', value='add_update_item')

    name.send_keys('Sprite')
    price.send_keys('5')
    quantity.send_keys('10')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Pepsi')
    price.send_keys('3')
    quantity.send_keys('3')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Fanta')
    price.send_keys('4')
    quantity.send_keys('8')
    add_update_item_button.click()

    time.sleep(0.5)

    row_1 = driver.find_elements(by='id', value='Sprite')
    row_2 = driver.find_elements(by='id', value='Pepsi')
    row_3 = driver.find_elements(by='id', value='Fanta')

    if len(row_1) != 1 or len(row_2) != 1 or len(row_3) != 1:
        res.fail_multiple('decrease/increase', "The page doesn't contain 3 rows with id 'Sprite', 'Pepsi' and 'Fanta'.", 9)
        return res
    else:
        res.succeed('decrease/increase')

    row_1_tds = row_1[0].find_elements(by='xpath', value='td')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    if len(row_1_tds) != 7 or len(row_2_tds) != 7 or len(row_3_tds) != 7:
        res.fail_multiple('decrease/increase', "At least 1 row doesn't contain 7 <td>.", 8)
        return res
    else:
        res.succeed('decrease/increase')

    row_1_tds[5].click()

    row_1 = driver.find_elements(by='id', value='Sprite')

    # print(row_1[0].find_element(by='xpath', value='td').text)

    row_2 = driver.find_elements(by='id', value='Pepsi')
    if len(row_1) != 1 or len(row_2) != 1:
        res.fail_multiple('decrease/increase', "The page doesn't contain 2 rows with id 'Sprite', 'Pepsi'.", 7)
        return res
    else:
        res.succeed('decrease/increase')
    row_1_tds = row_1[0].find_elements(by='xpath', value='td')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')

    if row_1_tds[0].text.strip() != "Sprite" or "5" not in row_1_tds[1].text or "11" not in row_1_tds[2].text or "55" not in row_1_tds[3].text:
        res.fail_multiple('decrease/increase', "Row 1 should contain Sprite (name), 5 (price), 11 (quantity), 55 (total).", 6)
        return res
    else:
        res.succeed('decrease/increase')

    row_2_tds[4].click()

    row_2 = driver.find_elements(by='id', value='Pepsi')
    if len(row_2) != 1:
        res.fail_multiple('decrease/increase', "The page doesn't contain 1 row with id 'Pepsi'.", 5)
        return res
    else:
        res.succeed('decrease/increase')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')

    row_2_tds[4].click()

    row_2 = driver.find_elements(by='id', value='Pepsi')
    if len(row_2) != 1:
        res.fail_multiple('decrease/increase', "The page doesn't contain 1 row with id 'Pepsi'.", 4)
        return res
    else:
        res.succeed('decrease/increase')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')

    row_2_tds[4].click()

    row_2 = driver.find_elements(by='id', value='Pepsi')
    if len(row_2) != 1:
        res.fail_multiple('decrease/increase', "The page doesn't contain 1 row with id 'Pepsi'.", 3)
        return res
    else:
        res.succeed('decrease/increase')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')

    row_2_tds[4].click()

    row_2 = driver.find_elements(by='id', value='Pepsi')
    row_3 = driver.find_elements(by='id', value='Fanta')
    if len(row_2) != 1 or len(row_3) != 1:
        res.fail_multiple('decrease/increase', "The page doesn't contain 2 rows with id 'Pepsi', 'Fanta'.", 2)
        return res
    else:
        res.succeed('decrease/increase')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    if row_2_tds[0].text.strip() != "Pepsi" or "3" not in row_2_tds[1].text or "0" not in row_2_tds[2].text or "0" not in row_2_tds[3].text:
        res.fail_multiple('decrease/increase', "Row 2 should contain Pepsi (name), 3 (price), 0 (quantity), 0 (total).", 1)
        return res
    else:
        res.succeed('decrease/increase')

    row_3_tds[4].click()

    row_3 = driver.find_elements(by='id', value='Fanta')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    row_3_tds[5].click()

    row_3 = driver.find_elements(by='id', value='Fanta')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    row_3_tds[4].click()

    row_3 = driver.find_elements(by='id', value='Fanta')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    row_3_tds[5].click()

    row_3 = driver.find_elements(by='id', value='Fanta')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    row_3_tds[5].click()

    row_3 = driver.find_elements(by='id', value='Fanta')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    if row_3_tds[0].text.strip() != "Fanta" or "4" not in row_3_tds[1].text or "9" not in row_3_tds[2].text or "36" not in row_3_tds[3].text:
        res.fail('decrease/increase', "Row 3 should contain Fanta (name), 4 (price), 9 (quantity), 36 (total).")
    else:
        res.succeed('decrease/increase')

    return res

