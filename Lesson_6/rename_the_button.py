from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

input_field = browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

button_txt = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located
    ((By.CSS_SELECTOR, ".btn-primary"))).text

print(button_txt) 

browser.quit()