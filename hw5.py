# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("http://ya.ru")
# driver.get("http://vk.com")
# driver.back() 
# sleep(30)


#зайти на сайт
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://labirint.ru")

#найти книги по питону, нажать enter
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)

#собрать все карточки
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print(len(books))

#вывести в консоль инфу (название, автор, цена)
for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text
    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
    except:
        author = "Автор не указан"
    print(author + "\t" + title + "\t" + price)


sleep(30)