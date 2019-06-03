import unittest

from common_lib.ui.driver_wrapper import Driver
from common_lib.ui.top_menu_bar.top_menu_bar_actions import TopMenuBarActions
from common_lib.ui.register_hotel_page.register_hotel_actions import RegisterHotelActions


class TestBaseUI(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()
        cls.top_menu_bar = TopMenuBarActions(cls.driver)
        cls.register_hotel_page = RegisterHotelActions(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
