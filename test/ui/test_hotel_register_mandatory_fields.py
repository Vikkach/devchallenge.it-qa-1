import pytest
from allure import step

from common_lib.ui.data_generator import DataGenerators
from common_lib.ui.default_data import EMPTY_DROPDOWN_FIELD
from common_lib.ui.register_hotel_page.attribute_to_fields_mapping import mandatory_fields, editable_dropdown_fields, \
    editable_date_fields
from test.ui import TestBaseRegisterHotel


class TestRegisterHotelMandatoryFields(TestBaseRegisterHotel):
    @pytest.mark.parametrize('asterisk_field', mandatory_fields)
    def test_field_marked_with_asterisk(self, asterisk_field, go_to_register_hotel_page):
        with step(f'Check {asterisk_field} field is marked as asterisk'):
            assert self.register_hotel_page.check_field_marked_as_asterisk(asterisk_field), \
                f'{asterisk_field} field should be marked with asterisk'

    @pytest.mark.parametrize('mandatory_field', mandatory_fields)
    def test_empty_mandatory_field(self, mandatory_field, go_to_register_hotel_page):
        with step('Fill all mandatory fields by correct values'):
            self.register_hotel_page.fill_registration_hotel_form_by_data()
        with step(f'Try to save the empty {mandatory_field} field'):
            if mandatory_field in editable_dropdown_fields:
                self.register_hotel_page.select_value_from_dropdown(mandatory_field, value=EMPTY_DROPDOWN_FIELD)
            else:
                self.register_hotel_page.type_text_to_field('', mandatory_field)
            self.register_hotel_page.click_on_save_button()
        with step('Check error message displayed'):
            assert self.register_hotel_page.check_error_message_is_present(mandatory_field), \
                f'{mandatory_field} error message should be present'

    def test_save_hotel_only_with_mandatory_fields(self, go_to_register_hotel_page,
                                                   generate_random_correct_mandatory_hotel_values):
        with step('Fill all mandatory fields by correct values'):
            self.register_hotel_page.fill_registration_hotel_form_by_data(
                random_values=generate_random_correct_mandatory_hotel_values)
        with step('Click on save button'):
            self.register_hotel_page.click_on_save_button()
        with step('Check hotel was saved in hotels list'):
            self.register_hotel_page.check_hotel_was_created(generate_random_correct_mandatory_hotel_values)

    @pytest.mark.parametrize('date_format_field', editable_date_fields)
    def test_save_incorrect_date_format_value(self, go_to_register_hotel_page, date_format_field,
                                              generate_random_correct_mandatory_hotel_values):
        with step('Fill all mandatory fields by correct values'):
            self.register_hotel_page.fill_registration_hotel_form_by_data(
                random_values=generate_random_correct_mandatory_hotel_values)
        with step(f'Try to save incorrect {date_format_field} field'):
            random_number = DataGenerators.generate_random_5_digit_number()
            self.register_hotel_page.type_text_to_field(random_number, date_format_field)
            self.register_hotel_page.click_on_save_button()
        with step('Check error message displayed'):
            assert self.register_hotel_page.check_error_message_is_present(date_format_field), \
                f'{date_format_field} error message should be present'
