from common_lib.ui.register_hotel_page.register_hotel_locators import RegisterHotelLocators

displayed_fields = {'Name': RegisterHotelLocators.name_field,
                    'Global Rating': RegisterHotelLocators.rating_field,
                    'Date of Construction': RegisterHotelLocators.date_of_construction_field,
                    'Country': RegisterHotelLocators.country_field,
                    'City': RegisterHotelLocators.city_field,
                    'Short Description': RegisterHotelLocators.short_description_field,
                    'Description': RegisterHotelLocators.description_field,
                    'Notes': RegisterHotelLocators.notes_field}

input_fields = {'Name': RegisterHotelLocators.name_input_field,
                'Date of Construction': RegisterHotelLocators.date_of_construction_input_field,
                'Country': RegisterHotelLocators.country_input_field,
                'City': RegisterHotelLocators.city_input_field,
                'Short Description': RegisterHotelLocators.short_description_input_field,
                'Description': RegisterHotelLocators.description_input_field,
                'Notes': RegisterHotelLocators.notes_input_field}

dropdown_value = {'Country': RegisterHotelLocators.country_dropdown_value,
                  'City': RegisterHotelLocators.city_dropdown_value}


asterisk_fields = {'Name': RegisterHotelLocators.name_field_asterisk,
                   'Date of Construction': RegisterHotelLocators.date_of_construction_field_asterisk,
                   'Country': RegisterHotelLocators.country_field_asterisk,
                   'City': RegisterHotelLocators.city_field_asterisk,
                   'Short Description': RegisterHotelLocators.short_description_field_asterisk,
                   'Description': RegisterHotelLocators.description_field_asterisk}

error_messages = {'Name': RegisterHotelLocators.name_error_message,
                   'Date of Construction': RegisterHotelLocators.date_of_construction_error_message,
                   'Country': RegisterHotelLocators.country_error_message,
                   'City': RegisterHotelLocators.city_error_message,
                   'Short Description': RegisterHotelLocators.short_description_error_message,
                   'Description': RegisterHotelLocators.description_error_message}