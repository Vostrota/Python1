import pytest
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Store:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")

    def user_name(self, value):
        self.browser.find_element(By.ID, "user-name").send_keys(value)
        sleep(3)

    def password(self, value):
        self.browser.find_element(By.ID, "password").send_keys(value)
        sleep(3)

    def login_button(self):
        self.browser.find_element(By.ID, "login-button").click()
        sleep(3)

    def add_sauce_labs_backpack(self):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        sleep(3)

    def add_sauce_labs_bolt_t_shirt(self):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        sleep(3)

    def add_sauce_labs_onesie(self):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        sleep(3)

    def open_cart(self):
        self.browser.find_element(By.ID, "shopping_cart_container").click()
        sleep(3)

    def click_checkout(self):
        self.browser.find_element(By.ID, "checkout").click()
        sleep(3)

    def first_name(self, value):
        self.browser.find_element(By.ID, "first-name").send_keys(value)
        sleep(3)

    def last_name(self, value):
        self.browser.find_element(By.ID, "last-name").send_keys(value)
        sleep(3)

    def postal_code(self, value):
        self.browser.find_element(By.ID, "postal-code").send_keys(value)
        sleep(3)
    
    def click_continue(self):
        self.browser.find_element(By.ID, "continue").click()
        sleep(3)
    
    def total_result(self):
        txt = self.browser.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
        return txt