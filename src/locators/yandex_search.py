from selenium.webdriver.common.by import By


class YandexSearch:
    CAPTCHA_IFRAME = (By.XPATH, "//iframe[@frameborder='0']")
    CAPTCHA_INPUT = (By.XPATH, "//input[@class='CheckboxCaptcha-Button']")
    SEARCH_INPUT_ON_YA_RU_PAGE = (By.XPATH, "//input[@id='text']")
    SEARCH_INPUT_ON_RESULT_PAGE = (By.XPATH, "//input[@name='text'][@role='combobox']")
    SUGGEST_TABLE = (By.XPATH, "//ul[@role='listbox']")
    ORG_HEADER_TITLE = (By.XPATH, "//h2[@id='orgHeaderTitle']")
    LINK_ON_YANDEX_SETTINGS = (By.XPATH, "//a[@href='//yandex.ru/tune/search']")
    NEXT_BUTTON_IN_PAGINATION = (By.XPATH, "//a[contains(text(), 'дальше')]")
    LINK_ON_TENSOR_WEB_SITE = (By.XPATH, "//li[@class='serp-item serp-item_card']//a[@href='https://tensor.ru/']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[@class='Button2 Button2_size_l Button2_view_default Button2_pin_circle-circle DistrSplashscreen-DeclineButtonOuter'][@type='button']")
    MENU_BUTTON = (By.XPATH, "//a[@title='Все сервисы']")
    IMAGES_BUTTON = (By.XPATH, "//a[@aria-label='Картинки']")
    FIRST_CATEGORY_BUTTON = (By.XPATH, "//div[@class='PopularRequestList-Shadow']")
    FIST_CATEGORY_TEXT = (By.XPATH, "//div[@class='PopularRequestList-SearchText']")
    LARGE_IMG_ON_IMAGES_PAGE = (By.XPATH, "//img[@class='MMImage-Origin']")
    NEXT_BUTTON_IN_IMG_MODAL = (By.XPATH, "//i[@class='CircleButton-Icon']")

    