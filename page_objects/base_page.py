import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Прогрузка элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести данные в поле')
    def input_text(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Переключение вкладок')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок')
    def get_page_header(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(*locator))

    @allure.step('Отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Прогрузка сайта Дзен')
    def wait_url_dzen(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    @allure.step('Получить URL')
    def get_current_url(self):
        return self.driver.current_url