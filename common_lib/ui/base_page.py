import os
import re

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config_parser import ConfigParser
from common_lib.ui.data_generator import DataGenerators
from common_lib.ui.default_data import DEFAULT_VALUES

TIMEOUT_SEC = 10


class BasePage:
    def __init__(self, driver):
        self.common_config = ConfigParser('/common.ini').config
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

    def is_editable(self, *locator, **kwargs):
        random_str = DataGenerators.generate_random_alphanumeric_str()
        if kwargs.get('date_format'):
            random_str = DEFAULT_VALUES.get('Date of Construction')
        self.type(random_str, *locator)
        return self.get_field_input_value(*locator) == random_str

    def type(self, text, *locator, **kwargs):
        self.wait_until_element_is_visible(locator)
        element = self.driver.find_element(*locator)
        if not kwargs.get('without_clear'):
            element.clear()
        element.send_keys(text)

    def open_dropdown_and_click_on_value(self, dropdown, dropdown_value):
        self.click(*dropdown)
        self.click(*dropdown_value)

    def get_field_input_value(self, *locator):
        return self.driver.find_element(*locator).get_attribute('value')

    def get_value_from_grid_or_dropdown(self, *locator):
        return self.driver.find_element(*locator).text
