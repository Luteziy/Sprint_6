from selenium.webdriver.common.by import By


class Locators:
    # Вопросы о важном
    QUESTIONS_ABOUT_IMPORTANT = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    SECTION = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    # Вопросы
    QUESTIONS = {
        0: [By.ID, 'accordion__heading-0'],  # Сколько это стоит? И как оплатить?
        1: [By.ID, 'accordion__heading-1'], # Хочу сразу несколько самокатов! Так можно?
        2: [By.ID, 'accordion__heading-2'], # Как рассчитывается время аренды?
        3: [By.ID, 'accordion__heading-3'], # Можно ли заказать самокат прямо на сегодня?
        4: [By.ID, 'accordion__heading-4'], # Можно ли продлить заказ или вернуть самокат раньше?
        5: [By.ID, 'accordion__heading-5'], # Вы привозите зарядку вместе с самокатом?
        6: [By.ID, 'accordion__heading-6'], # Можно ли отменить заказ?
        7: [By.ID, 'accordion__heading-7'] # Я жизу за МКАДом, привезёте?
    }

    ANSWER = {
        0: [By.ID, 'accordion__panel-0'],
        1: [By.ID, 'accordion__panel-1'],
        2: [By.ID, 'accordion__panel-2'],
        3: [By.ID, 'accordion__panel-3'],
        4: [By.ID, 'accordion__panel-4'],
        5: [By.ID, 'accordion__panel-5'],
        6: [By.ID, 'accordion__panel-6'],
        7: [By.ID, 'accordion__panel-7']
    }


    # Кнопка заказать (вверху страницы)
    ORDER_BUTTON_HEADER = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    # Кнопка заказать (внизу)
    ORDER_BUTTON_MAIN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    # Дзен URL
    DZEN_URL = 'https://dzen.ru/?yredirect=true'
    # Лого Самокат
    HEADER_LOGO_SCOOTER = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    # Лого Яндекс
    HEADER_LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    # Заголовок
    HEADER_MAIN = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')