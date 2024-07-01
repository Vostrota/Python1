from time import sleep
from selenium import webdriver

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

#Открыть сайт
driver.get("http://the-internet.herokuapp.com/inputs")

#Ввести "1000" в поле ввода, очистить поле, ввести "999"
search_field = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
sleep(5)
search_input.send_keys("1000")
sleep(5)
search_input.clear()
sleep(5)
search_input.send_keys("999")

sleep(5)

# Закрыть браузер
driver.quit()