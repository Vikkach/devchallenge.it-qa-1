import pytest
from allure import step, title

from common_lib.ui.register_hotel_page.attribute_to_fields_mapping import editable_input_fields, editable_date_fields, \
    alphanumeric_input_fields
from common_lib.ui.register_hotel_page.register_hotel_data_generator import RegisterHotelDataGenerator
from test.ui import TestBaseRegisterHotel


class TestRegisterHotelFieldsEditing(TestBaseRegisterHotel):
    @pytest.mark.parametrize('editable_field', editable_input_fields)
    @title('Test user can edit input fields')
    def test_input_field_is_editable(self, editable_field, go_to_register_hotel_page):
        with step(f'Check {editable_field} field is editable'):
            assert self.register_hotel_page.check_input_field_is_editable(editable_field), \
                f'{editable_field} field should be editable'

    @title('Test user can select value from dropdown fields (Country, City)')
    def test_dropdown_fields_are_editable(self, go_to_register_hotel_page):
        with step('Check Country dropdown field is editable'):
            assert self.register_hotel_page.check_dropdown_is_editable('Country'), \
                'Country dropdown field should be editable'
        # Cannot select City without Country
        with step('Check City dropdown field is editable'):
            assert self.register_hotel_page.check_dropdown_is_editable('City'), \
                'City dropdown field should be editable'

    @pytest.mark.parametrize('date_field', editable_date_fields)
    @title('Test user can edit date field')
    def test_date_field_is_editable(self, date_field, go_to_register_hotel_page):
        with step(f'Check {date_field} field is editable'):
            assert self.register_hotel_page.check_input_field_is_editable(date_field, date_format=True), \
                f'{date_field} field should be editable'


    @pytest.mark.parametrize('alphanumeric_field', alphanumeric_input_fields)
    @title('Test user can input alphanumeric characters to input fields')
    def test_input_fields_allows_alphanumeric_characters(self, alphanumeric_field, go_to_register_hotel_page):
        with step(f'Check {alphanumeric_field} field allows to input alphanumeric characters'):
            alphanumeric_str = RegisterHotelDataGenerator.generate_random_alphanumeric_str()
            assert self.register_hotel_page.type_text_to_field(alphanumeric_str, alphanumeric_field) == alphanumeric_str, \
                f'{alphanumeric_field} should allows to input alphanumeric characters'

    @title('Test user can save hotel with all valid data')
    def test_user_can_save_hotel_with_all_valid_data(self, go_to_register_hotel_page, generate_random_correct_hotel_values):
        with step('Fill all mandatory fields by correct values'):
            self.register_hotel_page.fill_registration_hotel_form_by_data(random_values=generate_random_correct_hotel_values)
        with step('Click on save button'):
            self.register_hotel_page.click_on_save_button()
        with step('Check hotel was saved in hotels list'):
            self.register_hotel_page.check_hotel_was_created(generate_random_correct_hotel_values)

