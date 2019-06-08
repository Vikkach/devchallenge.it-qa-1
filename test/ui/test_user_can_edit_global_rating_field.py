import pytest
from allure import step, title

from test.ui import TestBaseRegisterHotel


class TestUserCanEditGlobalRatingField(TestBaseRegisterHotel):
    @pytest.mark.parametrize('rating', [1, 2, 3, 4, 5])
    @title('Test user can save hotel with different rating')
    def test_user_can_rate_hotel(self, rating, go_to_register_hotel_page, generate_random_correct_hotel_values):
        with step('Set rating'):
            self.register_hotel_page.select_rating(rating)
        with step('Fill all mandatory fields and save hotel with rating'):
            self.register_hotel_page.fill_registration_hotel_form_by_data(random_values=generate_random_correct_hotel_values)
            self.register_hotel_page.click_on_save_button()
        with step(f'Check hotel was saved with rating {rating}'):
            assert int(self.register_hotel_page.get_rating_value_from_hotel_list(
                generate_random_correct_hotel_values)) == rating

    @title('Test user can save hotel without rating')
    def test_user_can_save_hotel_without_rating(self, go_to_register_hotel_page, generate_random_correct_hotel_values):
        with step('Fill all mandatory fields and save hotel without rating'):
            self.register_hotel_page.fill_registration_hotel_form_by_data(random_values=generate_random_correct_hotel_values)
            self.register_hotel_page.click_on_save_button()
        with step('Check hotel was saved with rating 0'):
            assert int(
                self.register_hotel_page.get_rating_value_from_hotel_list(generate_random_correct_hotel_values)) == 0
