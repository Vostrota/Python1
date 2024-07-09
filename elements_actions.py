from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://ya.ru")

element = browser.find_element(By.CSS_SELECTOR, "#text")
element.clear()
element.send_keys("VLADA")
sleep(5)
element.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

sleep(10)

# print(element)
#browser.find_elements()
# (session="0ae2524ec50ef4b74771d58cee89099c", element="f.3A66E6578EA4FAFF1796749D24C9A4EB.d.3FFAACCD0DC2B50BEED2AAB7D6CA900E.e.2")
browser.quit()