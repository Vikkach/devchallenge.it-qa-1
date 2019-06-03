from selenium.webdriver.common.by import By

class TopMenuBarLocators:
    article_tab = (By.XPATH, "//span[@class='ui-menuitem-text'][contains(.,'Article')]")
    new_tab = (By.XPATH, "//span[@class='ui-menuitem-text'][contains(.,'New')]")
    hotel_tab = (By.XPATH, "//span[@class='ui-menuitem-text'][./text()='Hotel']")
    data_section = (By.XPATH, "//form[@id='add_hotel']")
    save_button = (By.XPATH, "//button[contains(@id,'add_hotel')]")
