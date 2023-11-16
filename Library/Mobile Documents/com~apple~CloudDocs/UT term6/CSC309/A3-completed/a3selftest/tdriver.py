import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from tresult import TestResult

class TestDriver:
    def __init__(self, port: int, headless: bool=True, browser: str='chrome',
                 path: str='chromedriver'):
        self.port = port
        self.headless = headless
        self.url = f'http://127.0.0.1:{port}/'
        if browser == 'firefox':
            self.get_driver = self._firefox_driver
        elif browser == 'chrome':
            self.path = path
            self.get_driver = self._chrome_driver
        else:
            raise Exception("driver must be either chrome or firefox")

    def _firefox_driver(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
    
    def _chrome_driver(self):
        options = ChromeOptions()
        options.headless = self.headless
        service = ChromeService(self.path)
        return webdriver.Chrome(service=service, options=options)

    def run(self, function) -> TestResult:
        driver = self.get_driver()
        driver.get(self.url)
        driver.maximize_window()
        time.sleep(2)
        res: TestResult = function(driver)
        driver.quit()
        return res