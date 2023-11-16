import time, requests
from tresult import TestResult
from urllib.parse import urljoin

def test_like_simple(driver):
    res = TestResult()

    class_name_error = False
    likes = driver.find_elements(by='class name', value='like')

    if len(likes) <= 1:
        likes = driver.find_elements(by='class name', value='likes')
        class_name_error = True

    if len(likes) <= 1:
        res.fail_multiple('Q3 Like Increase 1', 'Cannot find elements with class name "like".', 7)
        return res
    else:
        res.succeed('Q3 Like Increase 1')

    text_before_1 = likes[0].text.strip()

    if text_before_1 == "":
        text_before_1 = likes[0].get_attribute("value")

        if text_before_1 is None:
            res.fail_multiple('Q3 Like Increase 1', 'There is no text in the like button.', 6)
            return res
        else:
            res.succeed('Q3 Like Increase 1')
    else:
        res.succeed('Q3 Like Increase 1')

    likes[0].click()

    time.sleep(1.5)

    likes = driver.find_elements(by='class name', value='like')

    if len(likes) <= 1:
        likes = driver.find_elements(by='class name', value='likes')
        class_name_error = True

    text_before_1_split = text_before_1.split(":")
    if len(text_before_1_split) != 2:
        res.fail_multiple('Q3 Like Increase 1', 'Cannot find ":" in the first like button.', 5)
        return res
    else:
        res.succeed('Q3 Like Increase 1')
    text_expected_num_1 = str(int(text_before_1_split[1]) + 1)

    text_before_2 = likes[1].text.strip()

    if text_before_2 == "":
        text_before_2 = likes[1].get_attribute("value")

        if text_before_2 is None:
            res.fail_multiple('Q3 Like Increase 1', 'There is no text in the like button.', 4)
            return res
        else:
            res.succeed('Q3 Like Increase 1')
    else:
        res.succeed('Q3 Like Increase 1')

    likes[1].click()

    time.sleep(1.5)

    likes = driver.find_elements(by='class name', value='like')

    if len(likes) <= 1:
        likes = driver.find_elements(by='class name', value='likes')
        class_name_error = True

    text_before_2_split = text_before_2.split(":")
    if len(text_before_2_split) != 2:
        res.fail_multiple('Q3 Like Increase 1', 'Cannot find ":" in the second like button.', 3)
        return res
    else:
        res.succeed('Q3 Like Increase 1')
    text_expected_num_2 = str(int(text_before_2_split[1]) + 1)
    time.sleep(1)

    if text_expected_num_1 not in likes[0].text.lower() and text_expected_num_1 not in likes[0].get_attribute("value"):
        actual_text = likes[0].text.lower()
        res.fail_multiple('Q3 Like Increase 1', 'The first like button displayed ' + text_before_1 + ' before. After one click, it should display ' + text_expected_num_1 + '. However, it is displaying ' + actual_text + '.', 2)
        return res
    else:
        res.succeed('Q3 Like Increase 1')

    if text_expected_num_2 not in likes[1].text.lower() and text_expected_num_2 not in likes[1].get_attribute("value"):
        actual_text = likes[1].text.lower()
        res.fail_multiple('Q3 Like Increase 1', 'The second like button displayed ' + text_before_2 + ' before. After one click, it should display ' + text_expected_num_2 + '. However, it is displaying ' + actual_text + '.', 1)
        return res
    else:
        res.succeed('Q3 Like Increase 1')

    if class_name_error:
        res.fail('Q3 Like Increase 1: Check "likes" spelling', "You use 'likes' instead of 'like' for class name")
    else:
        res.succeed('Q3 Like Increase 1: Check "likes" spelling')
    return res

def test_like_hard(driver):
    res = TestResult()
    class_name_error = False

    url = urljoin(driver.current_url, "text/like")
    data_para_1 = {"paragraph": 1}
    data_para_2 = {"paragraph": 2}
    requests.post(url, json=data_para_1)
    requests.post(url, json=data_para_2)

    likes = driver.find_elements(by='class name', value='like')

    if len(likes) <= 1:
        likes = driver.find_elements(by='class name', value='likes')
        class_name_error = True

    if len(likes) <= 1:
        res.fail_multiple('Q3 Like Increase 2', 'Cannot find elements with class name "like".', 7)
        return res
    else:
        res.succeed('Q3 Like Increase 2')

    text_before_1 = likes[0].text.strip()

    if text_before_1 == "":
        text_before_1 = likes[0].get_attribute("value")

        if text_before_1 is None:
            res.fail_multiple('Q3 Like Increase 2', 'There is no text in the like button.', 6)
            return res
        else:
            res.succeed('Q3 Like Increase 2')
    else:
        res.succeed('Q3 Like Increase 2')
    likes[0].click()

    time.sleep(1.5)

    likes = driver.find_elements(by='class name', value='like')

    if len(likes) <= 1:
        likes = driver.find_elements(by='class name', value='likes')
        class_name_error = True

    text_before_1_split = text_before_1.split(":")
    if len(text_before_1_split) != 2:
        res.fail_multiple('Q3 Like Increase 2', 'Cannot find ":" in the first like button.', 5)
        return res
    else:
        res.succeed('Q3 Like Increase 2')
    text_expected_num_1 = str(int(text_before_1_split[1]) + 2)

    text_before_2 = likes[1].text.strip()

    if text_before_2 == "":
        text_before_2 = likes[1].get_attribute("value")

        if text_before_2 is None:
            res.fail_multiple('Q3 Like Increase 2', 'There is no text in the like button.', 4)
            return res
        else:
            res.succeed('Q3 Like Increase 2')
    else:
        res.succeed('Q3 Like Increase 2')
    likes[1].click()

    time.sleep(1.5)

    likes = driver.find_elements(by='class name', value='like')

    if len(likes) <= 1:
        likes = driver.find_elements(by='class name', value='likes')
        class_name_error = True

    text_before_2_split = text_before_2.split(":")
    if len(text_before_2_split) != 2:
        res.fail_multiple('Q3 Like Increase 2', 'Cannot find ":" in the second like button.', 3)
        return res
    else:
        res.succeed('Q3 Like Increase 2')
    text_expected_num_2 = str(int(text_before_2_split[1]) + 2)
    time.sleep(1)

    if text_expected_num_1 not in likes[0].text.lower() and text_expected_num_1 not in likes[0].get_attribute("value"):
        actual_text = likes[0].text.lower()
        res.fail_multiple('Q3 Like Increase 2', 'The first like button displayed ' + text_before_1 + ' before. After one click from me and one click from another user, it should display ' + text_expected_num_1 + '. However, it is displaying ' + actual_text + '.', 2)
        return res
    else:
        res.succeed('Q3 Like Increase 2')

    if text_expected_num_2 not in likes[1].text.lower() and text_expected_num_2 not in likes[1].get_attribute("value"):
        actual_text = likes[1].text.lower()
        res.fail_multiple('Q3 Like Increase 2', 'The second like button displayed ' + text_before_2 + ' before. After one click from me and one click from another user, it should display ' + text_expected_num_2 + '. However, it is displaying ' + actual_text + '.', 1)
        return res
    else:
        res.succeed('Q3 Like Increase 2')

    if class_name_error:
        res.fail('Q3 Like Increase 2: Check "likes" spelling', "You use 'likes' instead of 'like' for class name")
    else:
        res.succeed('Q3 Like Increase 2: Check "likes" spelling')
    return res
