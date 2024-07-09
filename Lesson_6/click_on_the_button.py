from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.implicitly_wait(30)
browser.get("http://www.uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

green_bar = browser.find_element(By.CSS_SELECTOR, "#content")
txt = green_bar.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt) 

browser.quit()