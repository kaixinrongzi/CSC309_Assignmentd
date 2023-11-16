import time
from tresult import TestResult

def test_delete_item(driver):
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
        res.fail_multiple('Delete', "The page doesn't contain 3 rows with id 'Sprite', 'Pepsi' and 'Fanta'.", 9)
        return res
    else:
        res.succeed('Delete')

    row_1_tds = row_1[0].find_elements(by='xpath', value='td')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    if len(row_1_tds) != 7 or len(row_2_tds) != 7 or len(row_3_tds) != 7:
        res.fail_multiple('Delete', "At least 1 row doesn't contain 7 <td>.", 8)
        return res
    else:
        res.succeed('Delete')

    row_1_tds[6].click()

    row_2 = driver.find_elements(by='id', value='Pepsi')
    row_3 = driver.find_elements(by='id', value='Fanta')
    if len(row_2) != 1 or len(row_3) != 1:
        res.fail_multiple('Delete', "The page doesn't contain 2 rows with id 'Pepsi' and 'Fanta'.", 7)
        return res
    else:
        res.succeed('Delete')
    row_2_tds = row_2[0].find_elements(by='xpath', value='td')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    if len(driver.find_elements(by='id', value='Sprite')) != 0:
        res.fail_multiple('Delete', 'Old row 1 with id "Sprite" should be deleted.', 6)
        return res
    else:
        res.succeed('Delete')

    if row_2_tds[0].text.strip() != "Pepsi" or "3" not in row_2_tds[1].text or "3" not in row_2_tds[2].text or "9" not in row_2_tds[3].text:
        res.fail_multiple('Delete', "New row 1 should contain Pepsi (name), 3 (price), 3 (quantity), 9 (total).", 5)
        return res
    else:
        res.succeed('Delete')

    if row_3_tds[0].text.strip() != "Fanta" or "4" not in row_3_tds[1].text or "8" not in row_3_tds[2].text or "32" not in row_3_tds[3].text:
        res.fail_multiple('Delete', "New row 2 should contain Fanta (name), 4 (price), 8 (quantity), 32 (total).", 4)
        return res
    else:
        res.succeed('Delete')

    row_2_tds[6].click()

    row_3 = driver.find_elements(by='id', value='Fanta')
    if len(row_3) != 1:
        res.fail_multiple('Delete', "The page doesn't contain 1 row with id 'Fanta'.", 3)
        return res
    else:
        res.succeed('Delete')
    row_3_tds = row_3[0].find_elements(by='xpath', value='td')

    if len(driver.find_elements(by='id', value='Pepsi')) != 0:
        res.fail_multiple('Delete', 'Old row 1 with id "Pepsi" should be deleted.', 2)
        return res
    else:
        res.succeed('Delete')

    if row_3_tds[0].text.strip() != "Fanta" or "4" not in row_3_tds[1].text or "8" not in row_3_tds[2].text or "32" not in \
            row_3_tds[3].text:
        res.fail_multiple('Delete', "New row 1 should contain Fanta (name), 4 (price), 8 (quantity), 32 (total).", 1)
        return res
    else:
        res.succeed('Delete')

    row_3_tds[6].click()

    if len(driver.find_elements(by='id', value='Fanta')) != 0:
        res.fail('Delete', 'Old row 1 with id "Fanta" should be deleted.')
    else:
        res.succeed('Delete')

    return res
