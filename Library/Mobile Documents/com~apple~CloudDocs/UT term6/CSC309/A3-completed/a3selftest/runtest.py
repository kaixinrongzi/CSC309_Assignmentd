#!/usr/bin/env python

import signup, shop, paragraph
from typing import List
from tresult import TestResult
from tdriver import TestDriver
import sys        

def run_tests(tests: List, driver: TestDriver):
    for f in tests:
        res: TestResult = driver.run(f)
        for i in range(len(res.error_msgs)):
            err_msg = res.error_msgs[i]
            passed = err_msg is None
            yield {
                'name': res.test_cases[i],
                'output': 'Passed' if passed else err_msg,
                'status': 'pass' if passed else 'fail',
                'marks_earned': 1 if passed else 0,
                'marks_total': 1,
            }

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("usage: " + sys.argv[0] + " PORT [chrome|firefox]")
        sys.exit(1)
    
    port = int(sys.argv[1])
    browser = sys.argv[2] if len(sys.argv) == 3 else 'chrome'
    driver = TestDriver(port, browser=browser)

    total_marks = 0
    marks_earned = 0

    all_tests = signup.tests + shop.tests + paragraph.tests
    # all_tests = shop.tests
    for result in run_tests(all_tests, driver):
        # we don't currently tally total_marks because the tester can crash
        #total_marks += result['marks_total']
        marks_earned += result['marks_earned']
        total_marks += result['marks_total']
    print("\nYou received %d out of %d marks"%(marks_earned, total_marks))

