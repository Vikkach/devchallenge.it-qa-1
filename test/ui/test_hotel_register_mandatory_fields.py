from allure import step
import pytest

from common_lib.ui.default_data import EMPTY_DROPDOWN_FIELD
from test.ui import TestBaseRegisterHotel
from common_lib.ui.register_hotel_page.attribute_to_fields_mapping import mandatory_fields, editable_dropdown_fields


class TestRegisterHotelMandatoryFields(TestBaseRegisterHotel):
    @pytest.mark.parametrize('asterisk_field', mandatory_fields)
    def test_field_marked_with_asterisk(self, asterisk_field, go_to_register_hotel_page):
        with step(f'Check {asterisk_field} field is marked as asterisk'):
            assert self.register_hotel_page.check_field_marked_as_asterisk(asterisk_field), \
                f'{asterisk_field} field should be marked with asterisk'

    @pytest.mark.parametrize('mandatory_field', mandatory_fields)
    def test_empty_mandatory_field(self, mandatory_field, go_to_register_hotel_page):
        with step('Fill all mandatory fields by correct values'):
            self.register_hotel_page.fill_all_mandatory_fields_by_default_data()
        with step(f'Try to save the empty {mandatory_field} field'):
            if mandatory_field in editable_dropdown_fields:
                self.register_hotel_page.select_value_from_dropdown(mandatory_field, value=EMPTY_DROPDOWN_FIELD)
            else:
                self.register_hotel_page.type_text_to_field('', mandatory_field)
            self.register_hotel_page.click_on_save_button()
        with step('Check error message displayed'):
            assert self.register_hotel_page.check_error_message_is_present(mandatory_field), \
                f'{mandatory_field} error message should be present'