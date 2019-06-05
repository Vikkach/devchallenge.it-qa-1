from common_lib.ui.base_page import BasePage
from common_lib.ui.top_menu_bar.top_menu_bar_locators import TopMenuBarLocators


class TopMenuBarActions(BasePage):

    def go_to_welcome_page(self):
        self.open_page(self.common_config.get('ui_pages', 'welcome'))

    def move_to_article_tab(self):
        self.move_to_element(*TopMenuBarLocators.article_tab)

    def move_to_new_option(self):
        self.move_to_element(*TopMenuBarLocators.new_tab)

    def move_to_hotel_option(self):
        self.move_to_element(*TopMenuBarLocators.hotel_tab)

    def click_on_hotel_option(self):
        self.click(*TopMenuBarLocators.hotel_tab)



