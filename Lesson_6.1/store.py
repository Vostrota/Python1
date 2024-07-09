from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_form_internet_mag():
    browser.get("https://www.saucedemo.com/")
    browser.implicitly_wait(20)
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    sleep(3)
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    sleep(3)
    browser.find_element(By.ID, "login-button").click()
    sleep(3)
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    sleep(3)
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    sleep(3)
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    sleep(3)
    browser.find_element(By.ID, "shopping_cart_container").click()
    sleep(3)
    browser.find_element(By.ID, "checkout").click()
    sleep(3)
    browser.find_element(By.ID, "first-name").send_keys("Vlada")
    sleep(3)
    browser.find_element(By.ID, "last-name").send_keys("Vostrotina")
    sleep(3)
    browser.find_element(By.ID, "postal-code").send_keys("123007")
    sleep(3)
    browser.find_element(By.ID, "continue").click()
    sleep(3)
    txt = WebDriverWait(browser, "10").until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    browser.find_element(By.ID, "finish").click()
    sleep(3)
    
    assert txt == "Total: $58.29"

    browser.quit()