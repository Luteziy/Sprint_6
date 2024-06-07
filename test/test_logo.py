import allure
from locators.scooter_main_page_locators import Locators
from page_objects.scooter_main_page import ScooterMainPage


class TestLogoRegistrate:
    @allure.title('Проверка перехода на главную страницу по клику на лого "Самокат"')
    def test_click_logo_scooter_go_to_main_page(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.wait_visibility_of_header_logo_scooter()
        scooter_main_page.click_on_order_button_in_header()
        scooter_main_page.wait_visibility_of_header_logo_scooter()
        scooter_main_page.click_to_header_logo_scooter()
        scooter_main_page.wait_visibility_of_header_logo_scooter()
        assert scooter_main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзен" по клику на лого "Яндекс"')
    def test_click_logo_yandex_go_to_dzen(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.wait_visibility_of_header_logo_yandex()
        scooter_main_page.click_to_header_logo_yandex()
        scooter_main_page.switch_to_next_tab()
        scooter_main_page.wait_url_dzen(Locators.DZEN_URL)
        assert scooter_main_page.get_current_url() == Locators.DZEN_URL