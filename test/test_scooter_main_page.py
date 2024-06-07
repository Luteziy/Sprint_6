import allure
import pytest
from page_objects.scooter_main_page import ScooterMainPage
from data import Data

class Test_Scooter_Main_Page:

    @allure.title('Кликнуть по вопросу и узнать ответ')
    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize('question_num, answer', Data.test_data_answer_text)
    def test_click_question_check_text(self, driver, question_num, answer):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.scroll_to_section()
        scooter_main_page.wait_visibility_of_questions(question_num)
        scooter_main_page.click_on_question(question_num)
        scooter_main_page.wait_visibility_of_questions(question_num)
        assert scooter_main_page.get_displayed_text_from_answer(question_num) == answer