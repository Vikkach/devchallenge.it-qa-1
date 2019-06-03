from selenium.webdriver.common.by import By

class RegisterHotelLocators:
    register_hotel_name_field = (By.XPATH, "//input[@id='add_hotel:j_idt42']")
    register_hotel_name_field_asterisk = (By.XPATH, "//label[@id='add_hotel:j_idt42']/span[@class='ui-outputlabel-rfi']")
