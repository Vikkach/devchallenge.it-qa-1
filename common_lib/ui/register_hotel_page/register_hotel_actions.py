from common_lib.ui.base_page import BasePage
from common_lib.ui.register_hotel_page.register_hotel_locators import RegisterHotelLocators


class RegisterHotelActions(BasePage):
    def go_to_register_hotel_page(self):
        self.open_page(self.common_config.get('ui_pages', 'register_new_hotel'))

    def check_name_field_is_displayed(self):
        self.is_displayed(*RegisterHotelLocators.register_hotel_name_field)

    def check_name_marked_as_asterisk(self):
        self.is_displayed(*RegisterHotelLocators.register_hotel_name_field_asterisk)

    def check_name_is_editable(self):
        self.is_editable(*RegisterHotelLocators.register_hotel_name_field_asterisk)
