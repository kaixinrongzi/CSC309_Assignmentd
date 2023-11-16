import time
from tresult import TestResult

def test_update_item(driver):
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
    quantity.send_keys('5')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Sprite')
    price.send_keys('4')
    quantity.send_keys('100')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Pepsi')
    price.send_keys('2')
    quantity.send_keys('0')
    add_update_item_button.click()

    time.sleep(0.5)

    row_1 = driver.find_elements(by='id', value='Sprite')
    row_2 = driver.find_elements(by='id', value='Pepsi')

    if len(row_1) != 1 or len(row_2) != 1:
        res.fail('Update Item', "The page doesn't contain 2 rows with id 'Sprite' and 'Pepsi'.")
    else:
        res.succeed('Update Item')

    row_1_tds = row_1[0].find_elements(by='xpath', value='td') if len(row_1) > 0 else []
    row_2_tds = row_2[0].find_elements(by='xpath', value='td') if len(row_2) > 0 else []

    if len(row_1_tds) != 7 or len(row_2_tds) != 7:
        res.fail('Update Item', "At least 1 row doesn't contain 7 <td>.")
    else:
        res.succeed('Update Item')

    if len(row_1_tds) < 2:
        res.fail('Update Item', "Row 1 does not have enough columns for name, price, and quantity")
    elif row_1_tds[0].text.strip() != "Sprite" or "4" not in row_1_tds[1].text or "100" not in row_1_tds[2].text or "400" not in row_1_tds[3].text:
        res.fail('Update Item', "Row 1 should contain Sprite (name), 4 (price), 100 (quantity), 400 (total).")
    else:
        res.succeed('Update Item')

    if len(row_2_tds) < 2:
        res.fail('Update Item', "Row 2 does not have enough columns for name, price, and quantity")
    elif row_2_tds[0].text.strip() != "Pepsi" or "2" not in row_2_tds[1].text or "0" not in row_2_tds[2].text or "0" not in row_2_tds[3].text:
        res.fail('Update Item', "Row 2 should contain Pepsi (name), 2 (price), 0 (quantity), 0 (total).")
    else:
        res.succeed('Update Item')

    return res
