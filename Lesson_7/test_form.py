import pytest
from formPage import Form
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_form_fill():
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

    assert form.empty_zip_result_is_red()
    assert form.other_elements_result_is_green()

    browser.quit()


# def test_red_element():
#     browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     form = Form(browser)
#     form.first_name("Иван")
#     form.last_name("Петров")
#     form.adress("Ленина, 55-3")
#     form.email("test@skypro.com")
#     form.phone("+7985899998787")
#     form.zip_cod("")
#     form.city("Москва")
#     form.country("Россия")
#     form.job_position("QA")
#     form.company("SkyPro")
#     form.send_form()

#     assert form.empty_zip_result_is_red()
#     browser.quit()

# def test_green_elements():
#     browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     form = Form(browser)
#     form.first_name("Иван")
#     form.last_name("Петров")
#     form.adress("Ленина, 55-3")
#     form.email("test@skypro.com")
#     form.phone("+7985899998787")
#     form.zip_cod("")
#     form.city("Москва")
#     form.country("Россия")
#     form.job_position("QA")
#     form.company("SkyPro")
#     form.send_form()

#     assert form.other_elements_result_is_green()
#     browser.quit()




