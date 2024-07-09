from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

src = browser.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
print(src)

browser.quit()