from common_lib.ui.base_page import BasePage
from common_lib.base_logger import BaseLogger
from common_lib.ui.default_data import DEFAULT_VALUES
from common_lib.ui.register_hotel_page.attribute_to_fields_mapping import editable_dropdown_fields, mandatory_fields, \
    editable_date_fields, hotel_list_fields
from common_lib.ui.register_hotel_page.field_to_locator_mapping import displayed_fields, input_fields, dropdown_value, \
    asterisk_fields, error_messages
from common_lib.ui.register_hotel_page.register_hotel_locators import RegisterHotelLocators
from common_lib.ui.top_menu_bar.top_menu_bar_locators import TopMenuBarLocators


class RegisterHotelActions(BasePage):
    def go_to_register_hotel_page(self):
        BaseLogger.get_info_log('Go to register hotel page')
        self.open_page(self.common_config.get('ui_pages', 'register_new_hotel'))

    def check_data_section_is_present(self):
        BaseLogger.get_info_log('Check data section is present')
        return self.is_displayed(*TopMenuBarLocators.data_section)

    def check_save_button_is_present(self):
        BaseLogger.get_info_log('Check save button is present')
        return self.is_displayed(*TopMenuBarLocators.save_button)

    def click_on_save_button(self):
        BaseLogger.get_info_log('Click on save button')
        self.click(*TopMenuBarLocators.save_button)

    def check_field_is_displayed(self, field):
        BaseLogger.get_info_log(f'Check {field} field is displayed')
        locator = displayed_fields.get(field)
        return self.is_displayed(*locator)

    def check_input_field_is_editable(self, field, date_format=False):
        BaseLogger.get_info_log(f'Check {field} field is editable')
        locator = input_fields.get(field)
        return self.is_editable(*locator, date_format=date_format)

    def check_dropdown_is_editable(self, field):
        BaseLogger.get_info_log(f'Check {field} field is editable')
        test_value = DEFAULT_VALUES.get(field)
        selected_value = self.select_value_from_dropdown(field, value=test_value)
        return selected_value == test_value

    def select_value_from_dropdown(self, field, **kwargs):
        xref = list(dropdown_value.get(field))
        value = kwargs.get('value', DEFAULT_VALUES.get(field))
        xref[1] = xref[1].format(value)
        dropdown_value_locator = tuple(xref)
        dropdown_locator = input_fields.get(field)
        BaseLogger.get_info_log(f'Select value {value} from dropdown {field}')
        self.open_dropdown_and_click_on_value(dropdown_locator, dropdown_value_locator)
        return self.get_value_from_grid_or_dropdown(*dropdown_locator)

    def check_field_marked_as_asterisk(self, field):
        BaseLogger.get_info_log(f'Check {field} field is marked with asterisk')
        locator = asterisk_fields.get(field)
        return self.is_displayed(*locator)

    def type_text_to_field(self, text, field):
        BaseLogger.get_info_log(f'Type {text} to field {field}')
        locator = input_fields.get(field)
        self.type(text, *locator)
        return self.get_field_input_value(*locator)

    def check_error_message_is_present(self, field):
        BaseLogger.get_info_log(f'Check error message is present for field {field}')
        locator = error_messages.get(field)
        return self.is_displayed(*locator)

    def fill_registration_hotel_form_by_data(self, **kwargs):
        BaseLogger.get_info_log('Fill registration form by data')
        generated_hotel_values = kwargs.get('random_values', DEFAULT_VALUES)
        for field in mandatory_fields:
            if field in editable_dropdown_fields:
                self.select_value_from_dropdown(field)
            else:
                self.type_text_to_field(generated_hotel_values.get(field), field)
        return generated_hotel_values

    def check_hotel_was_created(self, saved_data):
        BaseLogger.get_info_log('Check hotel was created')
        self.click(*RegisterHotelLocators.go_to_end_button)
        for k, v in saved_data.items():
            if k not in editable_date_fields and k in hotel_list_fields:
                assert self.check_actual_value_in_hotels_grid(v)

    def check_actual_value_in_hotels_grid(self, value):
        BaseLogger.get_info_log(f'Check {value} is present in hotels grid')
        xref = list(RegisterHotelLocators.hotel_value)
        xref[1] = xref[1].format(value)
        locator = tuple(xref)
        return self.is_displayed(*locator)

    def select_rating(self, rating):
        BaseLogger.get_info_log(f'Select hotel rating: {rating}')
        xref = list(RegisterHotelLocators.rating_star)
        xref[1] = xref[1].format(rating)
        rating_star_locator = tuple(xref)
        self.click(*rating_star_locator)

    def get_rating_value_from_hotel_list(self, saved_values):
        self.click(*RegisterHotelLocators.go_to_end_button)
        hotel_name = saved_values.get('Name')
        BaseLogger.get_info_log(f'Get saved hotel rating for hotel with name {hotel_name}')
        xref = list(RegisterHotelLocators.rating_value_hotel_list)
        xref[1] = xref[1].format(hotel_name)
        locator = tuple(xref)
        return self.get_value_from_grid_or_dropdown(*locator)
