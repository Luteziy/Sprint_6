import allure
from locators.scooter_order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage
from data import Data

class ScooterOrderPage(BasePage):

    @allure.step('Ввод данных в блок "Для кого"')
    def input_block_for_whom(self, data):
        self.wait_visibility_of_element(OrderPageLocators.NAME)
        self.click_to_element(OrderPageLocators.NAME)
        self.input_text(OrderPageLocators.NAME, data[0])
        self.click_to_element(OrderPageLocators.SURNAME)
        self.input_text(OrderPageLocators.SURNAME, data[1])
        self.click_to_element(OrderPageLocators.ADRESS)
        self.input_text(OrderPageLocators.ADRESS, data[2])
        self.click_to_element(OrderPageLocators.METRO)
        self.input_text(OrderPageLocators.METRO, data[3])
        self.click_to_element(OrderPageLocators.STATION_LIST)
        self.click_to_element(OrderPageLocators.TELEPHONE)
        self.input_text(OrderPageLocators.TELEPHONE, data[4])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Клик по станции в выпадающем списке')
    def select_station(self):
        self.click_to_element(OrderPageLocators.STATION_LIST)

    @allure.step('Ввод даты заказа (Когда привезти самокат)')
    def input_data_when_scooter_arrive(self):
        self.input_text(OrderPageLocators.WHEN_SCOOTER_ARRIVE).send_keys(Data.test_data_user0[5])

    @allure.step('Клик по дате в выпадающем календаре')
    def click_date_in_calendar(self):
        self.click_to_element(OrderPageLocators.CALENDAR_ITEM)

    @allure.step('Проверить отображается ли кнопка "Посмотреть статус" после оформления заказа')
    def check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.CHECK_ORDER)

    @allure.step('Ввод данных в блок "Про Аренду"')
    def input_form_about_rent(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.WHEN_SCOOTER_ARRIVE)
        self.click_to_element(OrderPageLocators.WHEN_SCOOTER_ARRIVE)
        self.input_text(OrderPageLocators.WHEN_SCOOTER_ARRIVE, test_data[5])
        self.click_to_element(OrderPageLocators.CHECKBOX_GREY_COLOR)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.LIST_RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.COMMENT_FOR_COURIER)
        self.input_text(OrderPageLocators.COMMENT_FOR_COURIER, test_data[6])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_visibility_of_element(OrderPageLocators.CONFIRM_ORDER_CREATION)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_CREATION)