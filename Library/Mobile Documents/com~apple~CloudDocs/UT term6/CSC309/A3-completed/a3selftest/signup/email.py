import time
from tresult import TestResult

def test_email(driver):
    res = TestResult()

    # Setup
    email_input_box = driver.find_element(by='id', value='email')
    table = driver.find_element(by='id', value='cart-items')
    error = driver.find_element(by='id', value='email_notification')

    # TC1
    email_input_box.send_keys('Abc.example.com')
    table.click()
    time.sleep(0.5)
    if "email is invalid" not in error.text.lower():
        res.fail('Email: @ symbol change', '"Abc.example.com" should be rejected since it does not contain an @.')
    else:
        res.succeed('Email: @ symbol change')

    # TC2
    email_input_box.clear()
    email_input_box.send_keys('A@b@c@example.com')
    table.click()
    time.sleep(0.5)
    if "email is invalid" not in error.text.lower():
        res.fail('Email: multiple @ check', '"A@b@c@example.com" should be rejected since it contains more than one @ outside quotation marks.')
    else:
        res.succeed('Email: multiple @ check')

    # TC3
    email_input_box.clear()
    email_input_box.send_keys('John..Doe@example.com')
    table.click()
    time.sleep(0.5)
    if "email is invalid" not in error.text.lower():
        res.fail('Email: consecutive periods check', '"John..Doe@example.com" should be rejected since it contains consecutive dots.')
    else:
        res.succeed('Email: consecutive periods check')

    # TC4
    email_input_box.clear()
    email_input_box.send_keys('this\ still\"not\\allowed@example.com')
    table.click()
    time.sleep(0.5)
    if "email is invalid" not in error.text.lower():
        res.fail('Email: Invalid Chars', '"this\ still\"not\\allowed@example.com" should be rejected since spaces, quotes, and backslashes must be contained by quotes.')
    else:
        res.succeed('Email: Invalid Chars')

    # TC5
    email_input_box.clear()
    email_input_box.send_keys('i_like_underscore@but_its_not_allowed_in_this_part.example.com')
    table.click()
    time.sleep(0.5)
    if "email is invalid" not in error.text.lower():
        res.fail('Email: Underscore Check', '"i_like_underscore@but_its_not_allowed_in_this_part.example.com" should be rejected since underscore is not allowed in domain part.')
    else:
        res.succeed('Email: Underscore Check')

    # TC6
    email_input_box.clear()
    email_input_box.send_keys('mailhost!username@example.org')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        res.fail('Email: Valid Case', '"mailhost!username@example.org" should be accepted.')
    else:
        res.succeed('Email: Valid Case')

    # TC7
    email_input_box.clear()
    email_input_box.send_keys('hanxianxu.huang@utoronto.ca')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        res.fail('Email: Valid Case', '"hanxianxu.huang@utoronto.ca" should be accepted. (How can you fail this test???)')
    else:
        res.succeed('Email: Valid Case')

    # TC8
    email_input_box.clear()
    email_input_box.send_keys('hanxianxu.huang@mail.utoronto.ca')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        res.fail('Email: Valid Case', '"hanxianxu.huang@mail.utoronto.ca" should be accepted. (How can you fail this test???)')
    else:
        res.succeed('Email: Valid Case')

    # TC9
    email_input_box.clear()
    email_input_box.send_keys('disposable.style.email.with+symbol@example.com')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        res.fail('Email: Valid Case', '"disposable.style.email.with+symbol@example.com" should be accepted.')
    else:
        res.succeed('Email: Valid Case')

    # TC10
    email_input_box.clear()
    email_input_box.send_keys('user%example.com@example.org')
    table.click()
    time.sleep(0.5)
    if error.text.strip() != "":
        res.fail('Email: Valid Case', '"user%example.com@example.org" should be accepted.')
    else:
        res.succeed('Email: Valid Case')

    return res
