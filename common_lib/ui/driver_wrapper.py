import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Driver:
    @staticmethod
    def get_driver():
        try:
            browser = os.environ['BROWSER']
        except KeyError:
            os.environ['BROWSER'] = 'chrome'
            browser = os.environ['BROWSER']
        driver = None
        if browser == 'chrome':
            opt = Options()
            if os.getenv('HEADLESS_FLAG') == 'TRUE':
                opt.set_headless()
                opt.add_argument("--log-level=3")
                opt.add_argument("--enable-features=NetworkService")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1280, 720)
        return driver
