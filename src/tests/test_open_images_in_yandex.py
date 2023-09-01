from src.pages.yeandex_serach_page import YandexSearchPage
from src.pages.yandex_images_page import YandexImagesPage
from src.utils.add_driver import pass_driver
from time import sleep

@pass_driver
def test_open_images_in_yandex(driver=None):

    search = YandexSearchPage(driver)
    images_page = YandexImagesPage(driver)

    search.open_search_page()
    sleep(1)

    search.search_company()
    sleep(2)
    assert search.open_menu() == None, "Can not find menu button on ya.ru page"
    search.open_images()
    sleep(100)

    assert search.driver.current_url == 'https://ya.ru/images/', 'Current ulr not https://ya.ru/images/'
    category_text = images_page.open_fist_category()
    search_input_value = images_page.get_search_input_value()

    is_open_first_image, fist_image_src = images_page.is_open_image()

    assert category_text == search_input_value, 'Text in search input not like category title'
    sleep(1)
    assert is_open_first_image == True, 'Fist image no open'

    images_page.click_on_next_button()

    is_open_second_img = images_page.is_open_image()[0]

    assert is_open_second_img == True, 'Second image is not open'
    sleep(1)
    images_page.click_on_next_button()

    current_img_src = is_open_first_image()

    assert current_img_src == fist_image_src, 'Current image src not equal src of first img'





