from time import sleep
from selenium import webdriver

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

#Открыть сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#5 раз кликнуть на кнопку Add Element
for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
    sleep(10)

#Собрать со страницы список кнопок Delete  
add_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

#Вывести на экран размер списка
print('Размер списка кнопок Delete в браузере Chrome равен:', len(add_buttons))

sleep(10)

#Закрыть браузер
driver.quit()