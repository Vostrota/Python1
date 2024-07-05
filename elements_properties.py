from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://ya.ru")

#usd = browser.find_element(By.CSS_SELECTOR, "a[title*='USD']")
text = browser.find_element(By.CSS_SELECTOR, "a[data-statlog='2informers.stocks.item.1']").text
print(text)
tag = browser.find_element(By.CSS_SELECTOR, "a[data-statlog='2informers.stocks.item.1']").tag_name
print(tag)
id = browser.find_element(By.CSS_SELECTOR, "a[data-statlog='2informers.stocks.item.1']").id
print(id)
href = browser.find_element(By.CSS_SELECTOR, "a[data-statlog='2informers.stocks.item.1']").get_attribute("href")
print(href)
ff = browser.find_element(By.CSS_SELECTOR, "a[data-statlog='2informers.stocks.item.1']").value_of_css_property("font-family")
print(ff)
color = browser.find_element(By.CSS_SELECTOR, "a[data-statlog='2informers.stocks.item.1']").value_of_css_property("color")
print(color)

sleep(10)
browser.quit()