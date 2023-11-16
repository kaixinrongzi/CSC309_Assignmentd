import time
from tresult import TestResult

def test_total(driver):
    res = TestResult()

    # Setup
    name = driver.find_element(by='id', value='name')
    price = driver.find_element(by='id', value='price')
    quantity = driver.find_element(by='id', value='quantity')
    add_update_item_button = driver.find_element(by='id', value='add_update_item')
    subtotal = driver.find_element(by='id', value='subtotal')
    taxes = driver.find_element(by='id', value='taxes')
    grand_total = driver.find_element(by='id', value='grand_total')

    name.send_keys('Coca-Cola')
    price.send_keys('5')
    quantity.send_keys('10')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Coca-Cola')
    price.send_keys('3')
    quantity.send_keys('15')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Pepsi')
    price.send_keys('2')
    quantity.send_keys('5')
    add_update_item_button.click()

    name.clear()
    price.clear()
    quantity.clear()
    name.send_keys('Sprite')
    price.send_keys('1')
    quantity.send_keys('0')
    add_update_item_button.click()

    time.sleep(0.5)

    if ("55" not in subtotal.text.strip()) or ("7.15" not in taxes.text) or ("62.15" not in grand_total.text):
        res.fail('Q2 Subtotal Taxes Grand Total', "Subtotal should be 55. Taxes should be 7.15. Grand total should be 62.15.")
    else:
        res.succeed('Q2 Subtotal Taxes Grand Total')

    return res
