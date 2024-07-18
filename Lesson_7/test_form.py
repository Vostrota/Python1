import pytest
from time import sleep
from formPage import Form
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = Form(browser)
    form.first_name("Иван")
    form.last_name("Петров")
    form.adress("Ленина, 55-3")
    form.email("test@skypro.com")
    form.phone("+7985899998787")
    form.zip_cod("")
    form.city("Москва")
    form.country("Россия")
    form.job_position("QA")
    form.company("SkyPro")
    form.send_form()
    form.zip_cod_is_red()
    form.zip_cod_is_green()


