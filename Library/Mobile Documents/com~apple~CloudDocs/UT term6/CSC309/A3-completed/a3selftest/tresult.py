from typing import List
from dataclasses import dataclass, field

VERBOSE = True


@dataclass
class TestResult:
    total_mark: int = 0
    mark_earned: int = 0
    test_cases: List[str] = field(default_factory=list)
    error_msgs: List[str] = field(default_factory=list)

    def _new_test(self, test_case: str):
        self.total_mark += 1
        self.test_cases.append(test_case)
        if VERBOSE:
            print("%s ... " % test_case, end="")

    def succeed(self, test_case: str):
        self._new_test(test_case)
        self.mark_earned += 1
        self.error_msgs.append(None)
        if VERBOSE:
            print("PASS")

    def fail(self, test_case: str, error_msg: str):
        self._new_test(test_case)
        self.error_msgs.append(error_msg)
        if VERBOSE:
            print("FAIL\n\t" + error_msg)

    def fail_multiple(self, text_case: str, error_msg: str, num_subsequent_fail: int):
        """
        Fail multiple cases due to previous failure. num_fail is the number of extra tests failed, exclude current test
        """
        self.fail(text_case, error_msg)
        self.total_mark += num_subsequent_fail
        for i in range(num_subsequent_fail - 1):
            self._new_test(text_case)
            if VERBOSE:
                print("FAIL\n\t" + "Due to previous error")

