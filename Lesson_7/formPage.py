# import pytest
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# class Form:
#     def __init__(self, browser):
#         self.browser = browser
#         self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
#         self.browser.implicitly_wait(3)

#     def first_name(self, value):
#         self.browser.find_element(By.NAME, "first-name").send_keys(value)
    
#     def last_name(self, value):
#         self.browser.find_element(By.NAME, "last-name").send_keys(value)
    
#     def adress(self, value):
#         self.browser.find_element(By.NAME, "address").send_keys(value)
    
#     def email(self, value):
#         self.browser.find_element(By.NAME, "e-mail").send_keys(value)
    
#     def phone(self, value):
#         self.browser.find_element(By.NAME, "phone").send_keys(value)
    
#     def zip_cod(self, value):
#         self.browser.find_element(By.CSS_SELECTOR, "input.form-control[name='zip-code']").send_keys(value)

#     def city(self, value):
#         self.browser.find_element(By.NAME, "city").send_keys(value)
    
#     def country(self, value):
#         self.browser.find_element(By.NAME, "country").send_keys(value)
    
#     def job_position(self, value):
#         self.browser.find_element(By.NAME, "job-position").send_keys(value)
    
#     def company(self, value):
#         self.browser.find_element(By.NAME, "company").send_keys(value)
    
#     def send_form(self):
#         self.browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    
#     def empty_zip_result_is_red(self):
#         zip_code_element = self.browser.find_element(By.CSS_SELECTOR, "#zip-code")
#         class_list = zip_code_element.get_attribute("class").split(' ')
#         return 'alert-danger' in class_list

#     def other_elements_result_is_green(self):
#         elements = self.browser.find_elements(By.CSS_SELECTOR, "div.alert")
#         for el in elements:
#             id_element = el.get_attribute('id')
#             if id_element == 'zip-code':
#                 continue
#             class_list = el.get_attribute("class").split(' ')
#             if 'alert-success' in class_list:
#                 return True

        

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Form:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.browser.implicitly_wait(3)

    def first_name(self, value):
        self.browser.find_element(By.NAME, "first-name").send_keys(value)
    
    def last_name(self, value):
        self.browser.find_element(By.NAME, "last-name").send_keys(value)
    
    def adress(self, value):
        self.browser.find_element(By.NAME, "address").send_keys(value)
    
    def email(self, value):
        self.browser.find_element(By.NAME, "e-mail").send_keys(value)
    
    def phone(self, value):
        self.browser.find_element(By.NAME, "phone").send_keys(value)
    
    def zip_cod(self, value):
        self.browser.find_element(By.CSS_SELECTOR, "input.form-control[name='zip-code']").send_keys(value)

    def city(self, value):
        self.browser.find_element(By.NAME, "city").send_keys(value)
    
    def country(self, value):
        self.browser.find_element(By.NAME, "country").send_keys(value)
    
    def job_position(self, value):
        self.browser.find_element(By.NAME, "job-position").send_keys(value)
    
    def company(self, value):
        self.browser.find_element(By.NAME, "company").send_keys(value)
    
    def send_form(self):
        self.browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    
    def empty_zip_result_is_red(self):
        zip_code_element = self.browser.find_element(By.CSS_SELECTOR, "#zip-code")
        class_list = zip_code_element.get_attribute("class").split(' ')
        return 'alert-danger' in class_list

    def other_elements_result_is_green(self):
        elements = self.browser.find_elements(By.CSS_SELECTOR, "div.alert")
        for el in elements:
            id_element = el.get_attribute('id')
            if id_element == 'zip-code':
                continue
            class_list = el.get_attribute("class").split(' ')
            if 'alert-success' in class_list:
                return True

