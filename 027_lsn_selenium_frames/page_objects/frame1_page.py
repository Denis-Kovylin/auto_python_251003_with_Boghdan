from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException
import time


class Frame1Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_to_frame(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame1")

    def enter_secret_text(self, text="Frame1_Secret"):
        input_field = self.driver.find_element(By.ID, "input1")
        input_field.clear()
        input_field.send_keys(text)

    def click_verify_button(self):
        button = self.driver.find_element(By.TAG_NAME, "button")
        button.click()

    def get_alert_text_and_accept(self) -> str:
        # Ждём появления alert
        time.sleep(1)
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except NoAlertPresentException:
            raise AssertionError("❌ An alert was expected, but it didn't show up")
