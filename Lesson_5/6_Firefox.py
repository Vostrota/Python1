from time import sleep
from selenium import webdriver

#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Открыть сайт
driver.get(" http://the-internet.herokuapp.com/login")

#Ввести значение tomsmith в поле username
username = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username).send_keys("tomsmith")
sleep(5)

#Ввести значение SuperSecretPassword в поле password
password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password).send_keys("SuperSecretPassword!")
sleep(5)

#Нажать кнопку Login
button = driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(5)

#Закрыть браузер
driver.quit()