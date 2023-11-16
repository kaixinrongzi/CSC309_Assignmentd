import time
from tresult import TestResult

valid_items = [
    {'name': 'Coca-Cola better than Pepsi', 'price': '4.99', 'quantity' : '10'},
    {'name': 'Pepsi12345', 'price': '3', 'quantity' : '1'},
    {'name': 'Gummy 2000', 'price': '.25', 'quantity' : '0'},
]

valid_ids = [
    item['name'].replace(' ', '_') for item in valid_items
]

def test_add_item(driver):
    res = TestResult()

    # Setup
    name = driver.find_element(by='id', value='name')
    price = driver.find_element(by='id', value='price')
    quantity = driver.find_element(by='id', value='quantity')
    add_update_item_button = driver.find_element(by='id', value='add_update_item')

    for item in valid_items:   
        name.send_keys(item['name'])
        price.send_keys(item['price'])
        quantity.send_keys(item['quantity'])
        add_update_item_button.click()
        name.clear()
        price.clear()
        quantity.clear()

    time.sleep(0.5)

    rows = []
    for item_id in valid_ids:
        elem = driver.find_elements(by='id', value=item_id)
        rows.append(elem)

    passed = True
    for i, elem in enumerate(rows):
        num = len(elem)
        if num != 1:
            passed = False
            res.fail('Add Item', 
                     f"Found {num} rows with id '{valid_ids[i]}'. Should be exactly 1")
            break
    if passed:
        res.succeed('Add Item')


    tds = [ elem[0].find_elements(by='xpath', value='td') 
            if len(elem) > 0 else [] for elem in rows ]   
    passed = True
    for i, elem in enumerate(tds):
        num = len(elem)
        if num != 7:
            passed = False
            res.fail('Add Item', 
                     f"Found {num} <td> inside id '{valid_ids[i]}'. Should be exactly 7")
            break
    if passed:
        res.succeed('Add Item')   

    for i, item in enumerate(valid_items):
        if len(tds[i]) < 2:
            res.fail('Add Item', 
                     f"Row {i+1} does not have enough columns for name, price, and quantity")
            continue
        name = tds[i][0].text.strip()
        price = tds[i][1].text
        quantity = tds[i][2].text
        eprice = '$%.2f'%float(item['price'])
        if name != item['name']:
            res.fail('Add Item', 
                     f"Row {i+1} should contain {item['name']} (name), not {name}")
        elif price != eprice:
            res.fail('Add Item', 
                     f"Row {i+1} should contain {eprice} (price), not {price}")
        elif quantity != item['quantity']:
            res.fail('Add Item', 
                     f"Row {i+1} should contain {item['quantity']} (quantity), not {quantity}")
        else:
            res.succeed('Add Item')

    return res


