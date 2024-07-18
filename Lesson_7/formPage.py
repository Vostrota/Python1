import pytest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Form:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def first_name(self, value):
        self.browser.find_element(By.NAME, "first-name").send_keys(value)
        sleep(3)

    def last_name(self, value):
        self.browser.find_element(By.NAME, "last-name").send_keys(value)
        sleep(3)

    def adress(self, value):
        self.browser.find_element(By.NAME, "address").send_keys(value)
        sleep(3)

    def email(self, value):
        self.browser.find_element(By.NAME, "e-mail").send_keys(value)
        sleep(3)

    def phone(self, value):
        self.browser.find_element(By.NAME, "phone").send_keys(value)
        sleep(3)

    def zip_cod(self, value):
        self.browser.find_element(By.NAME, "zip-code").clear(value)
        sleep(3)

    def city(self, value):
        self.browser.find_element(By.NAME, "city").send_keys(value)
        sleep(3)

    def country(self, value):
        self.browser.find_element(By.NAME, "country").send_keys(value)
        sleep(3)

    def job_position(self, value):
        self.browser.find_element(By.NAME, "job-position").send_keys(value)
        sleep(3)

    def company(self, value):
        self.browser.find_element(By.NAME, "company").send_keys(value)
        sleep(3) 

    def send_form(self):
        self.browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        sleep(3)

    def zip_code_color(self):
        zip_id = self.browser.find_elements(By.CSS_SELECTOR, "#zip-code.alert-danger")
        return len(zip_id)

    def other_fields(self):
        fields = self.browser.find_elements(By.CSS_SELECTOR, "div.alert")
        for field in fields:
            id_field = field.get_attribute('id')
            if id_field == 'zip-code':
                continue
            class_list = field.get_attribute("class").split(' ')
            return class_list