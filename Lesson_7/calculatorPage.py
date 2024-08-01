import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class Calculator:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        input_delay = self.browser.find_element(By.ID, "delay")
        input_delay.clear()
        input_delay.send_keys(delay)

    def click_button(self, button):
        self.browser.find_element(By.XPATH, f'//span[contains(text(), {button})]').click()
    
    def wait_result(self, result):
        WebDriverWait(self.browser, "45").until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), result))
        return self.browser.find_element(By.CSS_SELECTOR, "div.screen").text
    