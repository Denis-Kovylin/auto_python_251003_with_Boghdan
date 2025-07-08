import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from page_objects.frame1_page import Frame1Page
from page_objects.frame2_page import Frame2Page


def test_verify_frames(driver):
    # Инициализация классов
    frame1 = Frame1Page(driver)
    frame2 = Frame2Page(driver)

    # Работа с первым фреймом
    frame1.switch_to_frame()
    frame1.enter_secret_text()
    frame1.click_verify_button()
    alert_text_1 = frame1.get_alert_text_and_accept()
    assert alert_text_1 == "Верифікація пройшла успішно!"

    # Работа со вторым фреймом
    frame2.switch_to_frame()
    frame2.enter_secret_text()
    frame2.click_verify_button()
    alert_text_2 = frame2.get_alert_text_and_accept()
    assert alert_text_2 == "Верифікація пройшла успішно!"
