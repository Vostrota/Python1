from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_form_calculator():
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.implicitly_wait(20)
    input_delay = browser.find_element(By.ID, "delay")
    input_delay.clear()
    input_delay.send_keys('45')
    sleep(3)
    browser.find_element(By.XPATH, '//span[contains(text(),"7")]').click()
    sleep(3)
    browser.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
    sleep(3)
    browser.find_element(By.XPATH, '//span[contains(text(),"8")]').click()
    sleep(3)
    browser.find_element(By.XPATH, '//span[contains(text(),"=")]').click()
    sleep(3)
    WebDriverWait(browser, "45").until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
    sleep(3)
    
    assert browser.find_element(By.CSS_SELECTOR, "div.screen").text == "15"
    
    browser.quit()