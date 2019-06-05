import pytest
from allure import step
from test import TestBaseUI


class TestBaseRegisterHotel(TestBaseUI):
    @pytest.fixture()
    def go_to_register_hotel_page(self):
        with step('Go to register hotel page'):
            self.register_hotel_page.go_to_register_hotel_page()

