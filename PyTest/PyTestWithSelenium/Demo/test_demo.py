from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
driver.get("https://www.lambdatest.com/selenium-playground/")

def test_load_page():
    driver.maximize_window()
    print(f"Title: {driver.title}")
    driver.close()