from allure import step

from test.ui import TestBaseRegisterHotel


class TestUserCanOpenRegisterHotelPage(TestBaseRegisterHotel):
    def test_user_can_open_register_hotel_page(self):
        with step('User open welcome page'):
            self.top_menu_bar.go_to_welcome_page()
        with step('User selects Articlr->New->Hotel'):
            self.top_menu_bar.move_to_article_tab()
            self.top_menu_bar.move_to_new_option()
            self.top_menu_bar.move_to_hotel_option()
            self.top_menu_bar.click_on_hotel_option()
        with step('Check Data section is present'):
            assert self.top_menu_bar.check_data_section_is_present(), \
                'Data section should be present on register hotel screen'
        with step('Check Save button is present'):
            assert self.top_menu_bar.check_save_button_is_present(), \
                'Save button should be present on register hotel screen'

