import allure
import pytest
from page_objects.scooter_order_page import ScooterOrderPage
from locators.scooter_main_page_locators import Locators
from data import Data

class TestOrderPage:
    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка возможности оформить заказ из двух точек входа')
    @pytest.mark.parametrize('butt, data', [(Locators.ORDER_BUTTON_HEADER, Data.test_data_user0),
                                           (Locators.ORDER_BUTTON_MAIN, Data.test_data_user1)])
    def test_order(self, driver, butt, data):
        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.scroll_to_element(butt)
        scooter_order_page.wait_visibility_of_element(butt)
        scooter_order_page.click_to_element(butt)
        scooter_order_page.input_block_for_whom(data)
        scooter_order_page.input_form_about_rent(data)
        assert scooter_order_page.check_status_of_order()