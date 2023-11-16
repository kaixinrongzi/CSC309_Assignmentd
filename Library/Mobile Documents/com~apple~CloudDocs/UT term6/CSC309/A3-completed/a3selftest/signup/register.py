import time
import uuid
from tresult import TestResult

def test_register(driver):
    res = TestResult()

    input_button = driver.find_element(by='id', value='register')
    table = driver.find_element(by='id', value='cart-items')
    error = driver.find_element(by='id', value='notification')
    username_error = driver.find_element(by='id', value='username_notification')

    input_button.click()
    time.sleep(0.5)
    if "at least one field is invalid. please correct it before proceeding" not in error.text.lower():
        # return '"At least one field is invalid. Please correct it before proceeding" is not in the page when the user clicks the register button without entering anything.'
        res.fail('Register', '"At least one field is invalid. Please correct it before proceeding" is not in the page when the user clicks the register button without entering anything.')
    else:
        res.succeed('Register')

    username = uuid.uuid4().hex[:12] + str(int(time.time()))

    input_box = driver.find_element(by='id', value='username')
    input_box.send_keys('Test' + username)
    input_box = driver.find_element(by='id', value='password1')
    input_box.send_keys('Test000!')
    input_box = driver.find_element(by='id', value='password2')
    input_box.send_keys('Test000!')
    input_box = driver.find_element(by='id', value='email')
    input_box.send_keys('test@utoronto.ca')
    input_box = driver.find_element(by='id', value='phone')
    input_box.send_keys('111-222-3333')
    table.click()

    input_button.click()
    time.sleep(2)
    if "user added" not in error.text.lower():
        # return '"User added" is not in the page after the user enters valid info and clicks the register button.'
        res.fail('Register', '"User added" is not in the page after the user enters valid info and clicks the register button.')
    else:
        res.succeed('Register')

    input_box = driver.find_element(by='id', value='username')
    input_box.clear()
    input_box.send_keys('Test' + username)
    input_box = driver.find_element(by='id', value='password1')
    input_box.clear()
    input_box.send_keys('Test000!')
    input_box = driver.find_element(by='id', value='password2')
    input_box.clear()
    input_box.send_keys('Test000!')
    input_box = driver.find_element(by='id', value='email')
    input_box.clear()
    input_box.send_keys('test@utoronto.ca')
    input_box = driver.find_element(by='id', value='phone')
    input_box.clear()
    input_box.send_keys('111-222-3333')
    table.click()

    input_button.click()
    time.sleep(2)
    if "username has already been taken" not in username_error.text.lower():
        # return '"Username has already been taken" is not in the page after the user enters clicks the register button again (without modifying anything).'
        res.fail('Register duplicate username', '"Username has already been taken" is not in the page after the user enters clicks the register button again (without modifying anything).')
    else:
        res.succeed('Register duplicate username')

    return res

