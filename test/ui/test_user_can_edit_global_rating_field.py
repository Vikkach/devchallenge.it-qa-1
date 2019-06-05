from allure import step
import pytest

from test.ui import TestBaseRegisterHotel


class TestUserCanEditGlobalRatingField(TestBaseRegisterHotel):
    @pytest.mark.parametrize('rating', [1, 2, 3, 4, 5])
    def test_user_can_rate_hotel(self, rating, go_to_register_hotel_page):
        with step('Set rating'):
            self.register_hotel_page.select_rating(rating)
        with step('Fill all mandatory fields and save hotel with rating'):
            self.register_hotel_page.fill_all_mandatory_fields_by_default_data()
            self.register_hotel_page.click_on_save_button()

    def test_user_can_save_hotel_without_rating(self, go_to_register_hotel_page):
        with step('Fill all mandatory fields and save hotel without rating'):
            self.register_hotel_page.fill_all_mandatory_fields_by_default_data()
            self.register_hotel_page.click_on_save_button()

