from src.pages.yeandex_serach_page import YandexSearchPage
from src.locators.yandex_search import YandexSearch
from src.utils.add_driver import pass_driver
from selenium.webdriver.common.keys import Keys
from time import sleep


@pass_driver
def test_search_link_on_company_web_page(driver=None):

    page = YandexSearchPage(driver)

    page.open_search_page()
    sleep(1)

    assert page.is_display_search_input() == True, 'Search input not display'

    page.search_company()
    sleep(1)

    assert page.is_display_suggest_table() == True, 'No display suggest table'

    page.send_keys_to_element(YandexSearch.SEARCH_INPUT_ON_YA_RU_PAGE, Keys.ENTER)
    sleep(1)
    page.close_set_yandex_default_browser()
    sleep(1)


    assert page.is_display_search_result_page() == True, 'Page with search result not display'
    sleep(1)
    assert page.is_first_lint_redirect_on_company_page() == True, 'First find element not have link on Tensor web page'





