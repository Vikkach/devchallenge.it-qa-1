import pytest
from allure import step

from common_lib.ui.register_hotel_page.attribute_to_fields_mapping import data_section_fields
from test.ui import TestBaseRegisterHotel


class TestRegisterHotelFieldsDisplaying(TestBaseRegisterHotel):
    @pytest.mark.parametrize('field', data_section_fields)
    def test_field_is_displayed_in_data_section(self, field, go_to_register_hotel_page):
        with step(f'Check {field} field is displayed'):
            assert self.register_hotel_page.check_field_is_displayed(field), \
                f'{field} field is not displayed in Data section of Register new Hotel page'
