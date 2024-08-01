import pytest
from calculatorPage import Calculator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = Calculator(browser)
    calculator.set_delay("1")
    calculator.click_button("7")
    calculator.click_button('"+"')
    calculator.click_button("8")
    calculator.click_button('"="')
    assert calculator.wait_result("15") == "15"
