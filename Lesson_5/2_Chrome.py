from time import sleep
from selenium import webdriver

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

#Открыть сайт
count = 0
driver.get(" http://uitestingplayground.com/dynamicid/")
sleep(5)

#Кликнуть на синюю кнопку и повторить действие 3 раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
    sleep(5)
    count = count + 1
    sleep(5)
    print("Нажатие ", count)

#Закрыть браузер
driver.quit()