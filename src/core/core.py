import requests
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.yandex_search import YandexSearch
from selenium.webdriver import ChromeOptions
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r'../chromedriver.exe'

class Core:

    def __init__(self, driver):
        self.driver = None
        if driver:
            self.driver = driver
        else:
            self.driver = Chrome

    def custom_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))


    def click_on_element(self, locator):
       self.custom_find_element(locator).click()


    def send_keys_to_element(self, locator, keys):
        element = self.custom_find_element(locator)
        element.send_keys(keys)

    def input_text(self, locator, text):
        element = self.custom_find_element(locator)
        element.send_keys(text)


    def is_display_captcha(self):
        element = self.custom_find_element(YandexSearch.CAPTCHA_IFRAME)
        return False

        if element:
            return None


