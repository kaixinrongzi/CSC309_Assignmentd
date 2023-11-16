import time
from tresult import TestResult

def test_password(driver):
    res = TestResult()

    # Setup
    table = driver.find_element(by='id', value='cart-items')
    password1_input_box = driver.find_element(by='id', value='password1')
    password2_input_box = driver.find_element(by='id', value='password2')
    error_1 = driver.find_element(by='id', value='password1_notification')
    error_2 = driver.find_element(by='id', value='password2_notification')

    # TC1
    password1_input_box.send_keys('Test!')
    table.click()
    time.sleep(0.5)
    if "password is invalid" not in error_1.text.lower():
        # driver.quit()
        # return '"Test!" should be rejected since it is too short.'
        res.fail('Password Length', '"Test!" should be rejected since it is too short.')
    else:
        res.succeed('Password Length')

    # TC2
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234')
    table.click()
    time.sleep(0.5)
    if "password is invalid" not in error_1.text.lower():
        # driver.quit()
        # return '"Test1234" should be rejected since it does not contain one sign.'
        res.fail('Password Symbol', '"Test1234" should be rejected since it does not contain one sign.')
    else:
        res.succeed('Password Symbol')

    # TC3
    password1_input_box.clear()
    password1_input_box.send_keys('test1234!')
    table.click()
    time.sleep(0.5)
    if "password is invalid" not in error_1.text.lower():
        # driver.quit()
        # return '"test1234!" should be rejected since it does not contain one uppercase letter.'
        res.fail('Password Uppercase', '"test1234!" should be rejected since it does not contain one uppercase letter.')
    else:
        res.succeed('Password Uppercase')

    # TC4
    password1_input_box.clear()
    password1_input_box.send_keys('TEST1234!')
    table.click()
    time.sleep(0.5)
    if "password is invalid" not in error_1.text.lower():
        # driver.quit()
        # return '"TEST1234!" should be rejected since it does not contain one lowercase letter.'
        res.fail('Password Lowercase', '"TEST1234!" should be rejected since it does not contain one lowercase letter.')
    else:
        res.succeed('Password Lowercase')

    # TC5
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234!')
    password2_input_box.clear()
    password2_input_box.send_keys('T')
    table.click()
    time.sleep(0.5)
    if "passwords don't match" not in error_2.text.lower():
        # driver.quit()
        # return "Passwords don't match is not in the page when password1 is Test1234! and password2 is T."
        res.fail('Password Match', "Passwords don't match is not in the page when password1 is Test1234! and password2 is T.")
    else:
        res.succeed('Password Match')

    # TC6
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234!')
    password2_input_box.clear()
    password2_input_box.send_keys('Test123')
    table.click()
    time.sleep(0.5)
    if "passwords don't match" not in error_2.text.lower():
        # driver.quit()
        # return "Passwords don't match is not in the page when password1 is Test1234! and password2 is Test123."
        res.fail('Password Match', "Passwords don't match is not in the page when password1 is Test1234! and password2 is Test123.")
    else:
        res.succeed('Password Match')

    # TC7
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234!')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234!')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234!" should be accepted.'
        res.fail('Password Pass Case 1', '"Test1234!" should be accepted.')
    else:
        res.succeed('Password Pass Case 1')

    # TC8
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234@')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234@')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234@" should be accepted.'
        res.fail('Password Pass Case 2', '"Test1234@" should be accepted.')
    else:
        res.succeed('Password Pass Case 2')

    # TC9
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234#')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234#')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234#" should be accepted.'
        res.fail('Password Pass Case 3', '"Test1234#" should be accepted.')
    else:
        res.succeed('Password Pass Case 3')

    # TC10
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234$')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234$')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234$" should be accepted.'
        res.fail('Password Pass Case 4', '"Test1234$" should be accepted.')
    else:
        res.succeed('Password Pass Case 4')

    # TC11
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234%')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234%')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234%" should be accepted.'
        res.fail('Password Pass Case 5', '"Test1234%" should be accepted.')
    else:
        res.succeed('Password Pass Case 5')

    # TC12
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234^')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234^')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234^" should be accepted.'
        res.fail('Password Pass Case 6', '"Test1234^" should be accepted.')
    else:
        res.succeed('Password Pass Case 6')

    # TC13
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234&')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234&')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234&" should be accepted.'
        res.fail('Password Pass Case 7', '"Test1234&" should be accepted.')
    else:
        res.succeed('Password Pass Case 7')

    # TC14
    password1_input_box.clear()
    password1_input_box.send_keys('Test1234*')
    password2_input_box.clear()
    password2_input_box.send_keys('Test1234*')
    table.click()
    time.sleep(0.5)
    if (error_1.text.strip() != "") or (error_2.text.strip() != ""):
        # driver.quit()
        # return '"Test1234*" should be accepted.'
        res.fail('Password Pass Case 8', '"Test1234*" should be accepted.')
    else:
        res.succeed('Password Pass Case 8')

    return res
