import time
from tresult import TestResult

def test_username(driver) -> TestResult:
    res = TestResult()

    # Setup
    username_input_box = driver.find_element(by='id', value='username')
    table = driver.find_element(by='id', value='cart-items')
    error = driver.find_element(by='id', value='username_notification')

    # TC1
    username_input_box.send_keys('test')
    table.click()
    time.sleep(0.5)
    if "username is invalid" not in error.text.lower():
        # driver.quit()
        res.fail("Username Test: length", '"test" should be rejected since it is too short.')
    else:
        res.succeed("Username Test: length")

    # TC2
    username_input_box.clear()
    username_input_box.send_keys('test0@')
    table.click()
    time.sleep(0.5)
    if "username is invalid" not in error.text.lower():
        res.fail("Username Test: invalid character", '"test0@" should be rejected since it contains @ which is invalid.')
    else:
        res.succeed("Username Test: invalid character")

    # TC3
    username_input_box.clear()
    username_input_box.send_keys('Test0_')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        # driver.quit()
        # return '"Test0_" should be accepted.'
        res.fail("Username Test: should succeed case", '"Test0_" should be accepted.')
    else:
        res.succeed("Username Test: should succeed case")

    # TC4
    username_input_box.clear()
    super_long = 'A' * 200
    username_input_box.send_keys(super_long)
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        res.fail("Username Test: super long username should be accepted", 
                f'"{super_long}" should be accepted.')
    else:
        res.succeed("Username Test: super long username should be accepted")

    return res
