from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

cookie = {
    'name': 'cookie-policy',
    'value': '1'
}


browser.get("https://labirint.ru")
browser.add_cookie(cookie)

cookie_n = browser.get_cookie('adrdel')
print(cookie_n)

# browser.refresh()
# browser.delete_all_cookies()

browser.quit()