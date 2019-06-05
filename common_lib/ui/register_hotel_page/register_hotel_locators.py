from selenium.webdriver.common.by import By


class RegisterHotelLocators:
    input_field_parent = "//input[@id='add_hotel:{}']"
    text_area_input_field_parent = "//textarea[@id='add_hotel:{}']"
    input_label_field_parent = "//label[@id='add_hotel:{}']"
    asteriks_parent = "//label[@for='add_hotel:{}']/span[@class='ui-outputlabel-rfi']"
    error_message_parent = "//div/span[contains(.,'{}')]"

    # Name
    name_field = (By.XPATH, "//label[@id='add_hotel:j_idt42']/../..")
    name_field_asterisk = (By.XPATH, asteriks_parent.format('name'))
    name_input_field = (By.XPATH, input_field_parent.format("name"))
    name_error_message = (By.XPATH, error_message_parent.format('Name'))

    # Global Rating
    rating_star = (By.XPATH, "(//div[@id='add_hotel:rate']/div[@class='ui-rating-star'])[{}]")
    rating_field = (By.XPATH, "//div[@id='add_hotel:rate']/..")

    # Date of Construction
    date_of_construction_input_field = (By.XPATH, input_field_parent.format("dateOfConstruction_input"))
    date_of_construction_field = (By.XPATH, "//span[@id='add_hotel:dateOfConstruction']/..")
    date_of_construction_field_asterisk = (By.XPATH, asteriks_parent.format('dateOfConstruction_input'))
    date_of_construction_error_message = (By.XPATH, error_message_parent.format('Date of Construction'))

    # Country
    country_input_field = (By.XPATH, input_label_field_parent.format("country_label"))
    country_dropdown_value = (By.XPATH,
                               "//div[@id='add_hotel:country_panel']//li[contains(@class,'ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all')][contains(.,'{}')]")
    country_field = (By.XPATH, "//div[@id='add_hotel:country']/..")
    country_field_asterisk = (By.XPATH, asteriks_parent.format('country_input'))
    country_error_message = (By.XPATH, error_message_parent.format('Country'))

    # City
    city_input_field = (By.XPATH, input_label_field_parent.format("city_label"))
    city_dropdown_value = (By.XPATH,
                              "//div[@id='add_hotel:city_panel']//li[contains(@class,'ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all')][contains(.,'{}')]")
    city_field = (By.XPATH, "//div[@id='add_hotel:city']/..")
    city_field_asterisk = (By.XPATH, asteriks_parent.format('city_input'))
    city_error_message = (By.XPATH, error_message_parent.format('City'))

    # Short Description
    short_description_input_field = (By.XPATH, input_field_parent.format("short_description"))
    short_description_field = (By.XPATH, "//input[@id='add_hotel:short_description']/..")
    short_description_field_asterisk = (By.XPATH, asteriks_parent.format('short_description'))
    short_description_error_message = (By.XPATH, error_message_parent.format('Short Description'))

    # Description
    description_input_field = (By.XPATH, text_area_input_field_parent.format("description"))
    description_field = (By.XPATH, "//textarea[@id='add_hotel:description']/..")
    description_field_asterisk = (By.XPATH, asteriks_parent.format('description'))
    description_error_message = (By.XPATH, error_message_parent.format('Description'))

    #Notes
    notes_field = (By.XPATH, "//textarea[@id='add_hotel:notes']/..")
    notes_input_field = (By.XPATH, text_area_input_field_parent.format("notes"))
