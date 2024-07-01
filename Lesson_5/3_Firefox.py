from time import sleep
from selenium import webdriver

#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Открыть сайт
driver.get("http://uitestingplayground.com/classattr/")
sleep(3)

#Найти и нажать на кнопку обработки всплывающего окна. Повторить действия три раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)
    driver.switch_to.alert.accept()
    sleep(5)

sleep(5)

#Закрыть браузер
driver.quit()