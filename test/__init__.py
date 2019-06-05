from common_lib.ui.driver_wrapper import Driver
from common_lib.ui.top_menu_bar.top_menu_bar_actions import TopMenuBarActions
from common_lib.ui.register_hotel_page.register_hotel_actions import RegisterHotelActions


class TestBaseUI:
    driver = None

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.top_menu_bar = TopMenuBarActions(self.driver)
        self.register_hotel_page = RegisterHotelActions(self.driver)

    def teardown_class(self):
        self.driver.quit()
