import time
from tresult import TestResult

def test_phone(driver):
    res = TestResult()

    # Setup
    phone_input_box = driver.find_element(by='id', value='phone')
    table = driver.find_element(by='id', value='cart-items')
    error = driver.find_element(by='id', value='phone_notification')

    # TC1
    phone_input_box.send_keys('1647-123-4567')
    table.click()
    time.sleep(0.5)
    if "phone is invalid" not in error.text.lower():
        # return '"1647-123-4567" should be rejected.'
        res.fail('Phone: Case 1', '"1647-123-4567" should be rejected.')
    else:
        res.succeed('Phone: Case 1')

    # TC2
    phone_input_box.clear()
    phone_input_box.send_keys('647-123-45678')
    table.click()
    time.sleep(0.5)
    if "phone is invalid" not in error.text.lower():
        # return '"647-123-45678" should be rejected.'
        res.fail('Phone: Case 2', '"647-123-45678" should be rejected.')
    else:
        res.succeed('Phone: Case 2')

    # TC3
    phone_input_box.clear()
    phone_input_box.send_keys('64a-123-4567')
    table.click()
    time.sleep(0.5)
    if "phone is invalid" not in error.text.lower():
        # return '"64a-123-4567" should be rejected.'
        res.fail('Phone: Case 3', '"64a-123-4567" should be rejected.')
    else:
        res.succeed('Phone: Case 3')

    # TC4
    phone_input_box.clear()
    phone_input_box.send_keys('6471234567')
    table.click()
    time.sleep(0.5)
    if "phone is invalid" not in error.text.lower():
        # return '"6471234567" should be rejected.'
        res.fail('Phone: Case 4', '"6471234567" should be rejected.')
    else:
        res.succeed('Phone: Case 4')

    # TC5
    phone_input_box.clear()
    phone_input_box.send_keys('.00-000-0000')
    table.click()
    time.sleep(0.5)
    if "phone is invalid" not in error.text.lower():
        # return '".00-000-0000" should be rejected.'
        res.fail('Phone: Case 5', '".00-000-0000" should be rejected.')
    else:
        res.succeed('Phone: Case 5')

    # TC6
    phone_input_box.clear()
    phone_input_box.send_keys('000-000-0000')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        # return '"000-000-0000" should be accepted.'
        res.fail('Phone: Case 6', '"000-000-0000" should be accepted.')
    else:
        res.succeed('Phone: Case 6')

    # TC7
    phone_input_box.clear()
    phone_input_box.send_keys('647-123-4567')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        # return '"647-123-4567" should be accepted.'
        res.fail('Phone: Case 7', '"647-123-4567" should be accepted.')
    else:
        res.succeed('Phone: Case 7')

    return res
