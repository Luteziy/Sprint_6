from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Для кого самокат_______________________________________
    title = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    # Поле имя
    NAME = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    # Поле фамилия
    SURNAME = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    # Поле "Адрес:куда привезти заказ"
    ADRESS = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    # Поле "Станция метро"
    METRO = (By.CSS_SELECTOR, "[placeholder='* Станция метро']")
    # Список станций метро
    STATION_LIST = (By.XPATH, ".//li[@class='select-search__row']")
    # Поле "Телефон: на него позвлнит курьер"
    TELEPHONE = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    NEXT_BUTTON = (By.CSS_SELECTOR, '.Button_Middle__1CSJM')

    # Про Аренду______________________________________________
    title_rent = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    # Поле "Когда привезти самокат"
    WHEN_SCOOTER_ARRIVE = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")
    # Поле Выбор даты(календарь)
    CALENDAR = (By.XPATH, "//div[@class='react-datepicker-popper']")
    # Выпадающее окно
    CALENDAR_ITEM = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    # Поле выбора срока аренды из выпадающего списка
    RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    # Выпадающий список
    LIST_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    # Чек-бокс
    CHECKBOX = (By.CLASS_NAME, 'Checkbox_Label__3wxSf')
    CHECKBOX_GREY_COLOR = (By.XPATH, "//input[@id='grey']")
    # Поле "Комментарий для курьера"
    COMMENT_FOR_COURIER = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")
    # Кнопка Заказать
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Хотите оформить заказ ?
    CONFIRM_ORDER_CREATION = (By.XPATH, "//button[.='Да']")
    # Окно Заказ оформлен
    MAKE_AN_ORDER = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]/div[@class="Order_ModalHeader__3FDaJ"]')
    # Посмотреть статус
    CHECK_ORDER = (By.XPATH, ".//*[text()='Посмотреть статус']")