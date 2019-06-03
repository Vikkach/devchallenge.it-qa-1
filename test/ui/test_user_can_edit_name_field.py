from allure import step

from test.ui import TestBaseRegisterHotel


class TestUserCanEditNameField(TestBaseRegisterHotel):
    def test_user_name_field(self):
        with step('Go to register hotel page'):
            self.register_hotel_page.go_to_register_hotel_page()
        with step('Check Name field is displayed'):
            assert self.register_hotel_page.check_name_field_is_displayed(), \
                'Name field is not displayed in Data section of Register new Hotel page'
        with step('Check Name field is marked as asterisk'):
            assert self.register_hotel_page.check_name_marked_as_asterisk(), \
                'Name field should be marked with asterisk'
        with step('Check Name field is editable'):
            assert self.register_hotel_page.check_name_is_editable(), \
                'Name field should be editable'



