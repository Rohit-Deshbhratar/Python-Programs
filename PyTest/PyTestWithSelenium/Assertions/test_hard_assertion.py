from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

class AssertionTest():
    pass

def test_select_gender():
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

    # Select gender
    driver.find_element(By.XPATH, "//h4[contains(text(), 'Gender')]"
                                  " //following::input[@value='Male']").click()

    # Select age group
    driver.find_element(By.XPATH, "//h4[contains(text(), 'Age : ')]"
                                  "//following::input[@value='15 - 50']").click()

    # Click button
    driver.find_element(By.XPATH, "//button[text()='Get values']").click()

    # Get selected values after clicking
    gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
    age_group = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton").text

    # Printing object ids
    print(f"Gender object: {id(gender)}")
    print(f"Male object: {id('Male')}")
    print(f"Age group object: {id(age_group)}")
    print(f"15 - 50 object: {id('15 - 50')}")

    # Compare values selected earlier
    assert gender == "Male", "Selected gender is not correct"
    assert age_group == "15 - 50", "Not in age group"
    assert driver.title.__contains__("Selenium Grid Online")

    driver.close()
