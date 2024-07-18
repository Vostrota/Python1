import pytest
from storePage import Store
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_store():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    store = Store(browser)
    store.user_name("standard_user")
    store.password("secret_sauce")
    store.login_button()
    store.add_sauce_labs_backpack()
    store.add_sauce_labs_bolt_t_shirt()
    store.add_sauce_labs_onesie()
    store.open_cart()
    store.click_checkout()
    store.first_name("Vlada")
    store.last_name("Vostrotina")
    store.postal_code("123007")
    store.click_continue()
    store.total_result()
