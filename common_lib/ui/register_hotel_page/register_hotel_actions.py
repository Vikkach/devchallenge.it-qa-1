from common_lib.ui.default_data import DEFAULT_VALUES
from common_lib.ui.base_page import BasePage
from common_lib.ui.register_hotel_page.register_hotel_locators import RegisterHotelLocators
from common_lib.ui.top_menu_bar.top_menu_bar_locators import TopMenuBarLocators
from common_lib.ui.register_hotel_page.field_to_locator_mapping import displayed_fields, input_fields, dropdown_value, asterisk_fields, error_messages
from common_lib.ui.register_hotel_page.attribute_to_fields_mapping import editable_dropdown_fields, mandatory_fields



class RegisterHotelActions(BasePage):
    def go_to_register_hotel_page(self):
        self.open_page(self.common_config.get('ui_pages', 'register_new_hotel'))

    def check_data_section_is_present(self):
        return self.is_displayed(*TopMenuBarLocators.data_section)

    def check_save_button_is_present(self):
        return self.is_displayed(*TopMenuBarLocators.save_button)

    def click_on_save_button(self):
        self.click(*TopMenuBarLocators.save_button)

    def check_field_is_displayed(self, field):
        locator = displayed_fields.get(field)
        return self.is_displayed(*locator)

    def check_input_field_is_editable(self, field, date_format=False):
        locator = input_fields.get(field)
        return self.is_editable(*locator, date_format=date_format)

    def check_dropdown_is_editable(self, field):
        test_value = DEFAULT_VALUES.get(field)
        selected_value = self.select_value_from_dropdown(field, value=test_value)
        return selected_value == test_value

    def select_value_from_dropdown(self, field, **kwargs):
        xref = list(dropdown_value.get(field))
        value = kwargs.get('value', DEFAULT_VALUES.get(field))
        xref[1] = xref[1].format(value)
        dropdown_value_locator = tuple(xref)
        dropdown_locator = input_fields.get(field)
        self.open_dropdown_and_click_on_value(dropdown_locator, dropdown_value_locator)
        return self.get_dropdown_field_selected_value(*dropdown_locator)

    def check_field_marked_as_asterisk(self, field):
        locator = asterisk_fields.get(field)
        return self.is_displayed(*locator)

    def type_text_to_field(self, text, field):
        locator = input_fields.get(field)
        self.type(text, *locator)
        return self.get_field_input_value(*locator)

    def check_error_message_is_present(self, field):
        locator = error_messages.get(field)
        return self.is_displayed(*locator)



    def check_name_marked_as_asterisk(self):
        return self.is_displayed(*RegisterHotelLocators.name_field_asterisk)

    def check_name_error_message_is_present(self):
        return self.is_displayed(*RegisterHotelLocators.name_error_message)

    def type_text_to_name_field(self, text):
        self.type(text, *RegisterHotelLocators.name_input_field)

    def type_text_to_date_of_construction_field(self, text=DEFAULT_VALUES):
        self.type(text, *RegisterHotelLocators.date_of_construction_input_field)

    def type_text_to_short_description_field(self, text):
        self.type(text, *RegisterHotelLocators.short_description_input_field)

    def type_text_to_description_field(self, text):
        self.type(text, *RegisterHotelLocators.description_input_field)

    def select_country(self, value=DEFAULT_VALUES):
        xref = list(RegisterHotelLocators.country_dropdown_value)
        xref[1] = xref[1].format(value)
        dropdown_value_locator = tuple(xref)
        self.open_dropdown_and_click_on_value(RegisterHotelLocators.country_input_field, dropdown_value_locator)

    def select_city(self, value=DEFAULT_VALUES):
        xref = list(RegisterHotelLocators.city_dropdown_value)
        xref[1] = xref[1].format(value)
        dropdown_value_locator = tuple(xref)
        self.open_dropdown_and_click_on_value(RegisterHotelLocators.city_input_field, dropdown_value_locator)

    def fill_all_mandatory_fields_by_default_data(self):
        for field in mandatory_fields:
            if field in editable_dropdown_fields:
                self.select_value_from_dropdown(field)
            else:
                self.type_text_to_field(DEFAULT_VALUES.get(field), field)


    def select_rating(self, rating):
        xref = list(RegisterHotelLocators.rating_star)
        xref[1] = xref[1].format(rating)
        rating_star_locator = tuple(xref)
        self.click(*rating_star_locator)


