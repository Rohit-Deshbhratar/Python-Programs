from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
driver.get("https://ecommerce-playground.lambdatest.io/")

def test_ecommerce():
    driver.maximize_window()
    print(f"Title: {driver.title}")
    driver.close()