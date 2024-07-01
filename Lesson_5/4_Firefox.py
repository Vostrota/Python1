from time import sleep
from selenium import webdriver

#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Открыть сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

#Нажать кнопку Сlose в модальном окне
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(5)

#Закрыть браузер
driver.quit()