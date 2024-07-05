from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def make_screenshot(browser):
    browser.maximize_window()
    browser.get("https:/ya.ru")
    sleep(5)

    browser.save_screenshot('.ya_'+browser.name+'.png')
    browser.quit()

edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

make_screenshot(edge)
make_screenshot(chrome)