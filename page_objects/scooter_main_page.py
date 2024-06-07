from page_objects.base_page import BasePage
from locators.scooter_main_page_locators import Locators
import allure

class ScooterMainPage(BasePage):
    @allure.step('Ожидание прогрузки кнопки "Заказать" в заголовке')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(Locators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по кнопке "Заказать" в заголовке')
    def click_on_order_button_in_header(self):
        self.click_to_element(Locators.ORDER_BUTTON_HEADER)

    @allure.step('Ожидание прогрузки лого с надписью "Самокат" в заголовке')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(Locators.HEADER_LOGO_SCOOTER)

    @allure.step('Ожидание прогрузки лого с надписью "Яндекс" в заголовке')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(Locators.HEADER_LOGO_YANDEX)

    @allure.step('Клик по элементу "Самокат" в заголовке')
    def click_to_header_logo_scooter(self):
        self.click_to_element(Locators.HEADER_LOGO_SCOOTER)

    @allure.step('Клик по элементу "Яндекс" в заголовке')
    def click_to_header_logo_yandex(self):
        self.click_to_element(Locators.HEADER_LOGO_YANDEX)

    @allure.step('Ожидание загрузки заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(Locators.HEADER_MAIN)

    @allure.step('Отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(Locators.HEADER_MAIN)

    @allure.step('Скролл до "Вопросы о важном"')
    def scroll_to_section(self):
        self.scroll_to_element(Locators.SECTION)

    @allure.step('Ожидание нужного вопроса')
    def wait_visibility_of_questions(self, data):
        self.wait_visibility_of_element(Locators.QUESTIONS[data])

    @allure.step('Клик по вопросу')
    def click_on_question(self, data):
        self.click_to_element(Locators.QUESTIONS[data])

    @allure.step('Ожидание загрузки ответа')
    def wait_visibility_of_answer(self, data):
        self.wait_visibility_of_element(Locators.ANSWER[data])

    @allure.step('Получить текст ответа')
    def get_displayed_text_from_answer(self, data):
        return self.get_text_from_element(Locators.ANSWER[data])