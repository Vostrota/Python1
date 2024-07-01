from time import sleep
from selenium import webdriver

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

#Открыть сайт
driver.get("http://uitestingplayground.com/classattr/")
sleep(5)

#Найти и нажать на кнопку обработки всплывающего окна. Повторить действия 3 раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(5)
    driver.switch_to.alert.accept()
    sleep(5)

sleep(5)

#Закрыть браузер
driver.quit()