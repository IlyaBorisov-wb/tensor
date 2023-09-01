from src.locators.yandex_search import YandexSearch
from src.core.core import Core

YANDEX_SEARCH_URL = 'https://ya.ru'

class YandexSearchPage(Core):

    def open_search_page(self):
        self.driver.get(YANDEX_SEARCH_URL)

    def is_display_search_input(self):
        return self.custom_find_element(YandexSearch.SEARCH_INPUT_ON_YA_RU_PAGE) != None

    def search_company(self):
        self.input_text(YandexSearch.SEARCH_INPUT_ON_YA_RU_PAGE, 'Тензор')

    def open_menu(self):
        self.custom_find_element(YandexSearch.MENU_BUTTON).click()

    def open_images(self):
        self.custom_find_element(YandexSearch.IMAGES_BUTTON).click()

    def close_set_yandex_default_browser(self):
        element = self.custom_find_element(YandexSearch.CLOSE_MODAL_BUTTON)
        if element:
            element.click()
        return

    def is_display_suggest_table(self):
        return self.custom_find_element(YandexSearch.SUGGEST_TABLE) != None

    def is_display_search_result_page(self):
        settings_button = self.custom_find_element(YandexSearch.LINK_ON_YANDEX_SETTINGS)
        next_button = self.custom_find_element(YandexSearch.NEXT_BUTTON_IN_PAGINATION)

        return settings_button != None and next_button != None


    def is_first_lint_redirect_on_company_page(self):
        return self.custom_find_element(YandexSearch.LINK_ON_TENSOR_WEB_SITE) != None

