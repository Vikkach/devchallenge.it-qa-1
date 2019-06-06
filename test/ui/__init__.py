import pytest
from allure import step

from common_lib.ui.data_generator import DataGenerators
from test import TestBaseUI


class TestBaseRegisterHotel(TestBaseUI):
    @pytest.fixture()
    def go_to_register_hotel_page(self):
        with step('Go to register hotel page'):
            self.register_hotel_page.go_to_register_hotel_page()

    @pytest.fixture()
    def generate_random_correct_hotel_values(self):
        with step('Generate random hotel and return it'):
            return {'Name': f'Automation Test Name {DataGenerators.generate_random_alphanumeric_str()}',
                    'Date of Construction': '1/1/01',
                    'Country': 'Ukraine',
                    'City': 'Kyiv',
                    'Description': f'Automation Test Description {DataGenerators.generate_random_alphanumeric_str()}',
                    'Short Description': f'Automation Test Short Description {DataGenerators.generate_random_alphanumeric_str()}',
                    'Note': f'Automation Test Note {DataGenerators.generate_random_alphanumeric_str()}'}

    @pytest.fixture()
    def generate_random_correct_mandatory_hotel_values(self):
        with step('Generate random hotel and return it'):
            return {'Name': f'Automation Test Name {DataGenerators.generate_random_alphanumeric_str()}',
                    'Date of Construction': '1/1/01',
                    'Country': 'Ukraine',
                    'City': 'Kyiv',
                    'Description': f'Automation Test Description {DataGenerators.generate_random_alphanumeric_str()}',
                    'Short Description': f'Automation Test Short Description {DataGenerators.generate_random_alphanumeric_str()}'}
