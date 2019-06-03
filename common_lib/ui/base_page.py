import os
import re

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config_parser import ConfigParser

TIMEOUT_SEC = 10


class BasePage:
    def __init__(self, driver):
        self.common_config = ConfigParser('\\common.ini').config
        self.root_url = self.common_config.get('main_url', 'main_url')
        self.driver = driver

    def get_driver_version(self):
        if os.environ['BROWSER'] == 'chrome':
            return re.findall(r'(\w+.\w+.\w+.\w+) ', self.driver.capabilities['chrome']['chromedriverVersion'])[0]
        elif os.environ['BROWSER'] == 'firefox':
            return self.driver.capabilities['moz:geckodriverVersion']

    def open_page(self, url=""):
        try:
            self.driver.get('{}{}'.format(self.root_url, url))
        except TimeoutException:
            self.driver.refresh()

    def click(self, *locator):
        self.wait_until_element_is_visible(locator)
        self.driver.find_element(*locator).click()

    def move_to_element(self, *locator):
        self.wait_until_element_is_visible(locator)
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def is_displayed(self, *locator):
        return self.driver.find_element(*locator).is_displayed()

    def wait_until_element_is_visible(self, locator, timeout=TIMEOUT_SEC):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Element {locator} missed. It takes more than {timeout} sec to load an element')

    def is_editable(self, *locator):
        return self.driver.find_element(*locator).is_editble()
