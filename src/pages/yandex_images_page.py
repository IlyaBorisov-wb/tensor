from src.core.core import Core
from src.locators.yandex_search import YandexSearch

class YandexImagesPage(Core):

    def open_fist_category(self):
        self.custom_find_element(YandexSearch.FIRST_CATEGORY_BUTTON)
        return self.custom_find_element(YandexSearch.FIRST_CATEGORY_BUTTON).text

    def get_search_input_value(self):
       return self.custom_find_element(YandexSearch.SEARCH_INPUT_ON_RESULT_PAGE).value

    def open_first_image(self):
        self.custom_find_element(YandexSearch.FIRST_CATEGORY_BUTTON).click()

    def is_open_image(self):
        element = self.custom_find_element(YandexSearch.LARGE_IMG_ON_IMAGES_PAGE)
        img_src = element.get_attribute('src')
        return len(img_src) > 0, img_src

    def is_open_next_image(self):
        return len(self.custom_find_element(YandexSearch.LARGE_IMG_ON_IMAGES_PAGE).get_attribute('src')) > 0

    def click_on_back_button(self):
        self.custom_find_element(YandexSearch.NEXT_BUTTON_IN_IMG_MODAL)

    def click_on_next_button(self):
        self.custom_find_element(YandexSearch.NEXT_BUTTON_IN_IMG_MODAL)

