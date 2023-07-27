import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

class AssertionTest(softest.TestCase):
    pass

    def test_select_gender(self):
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
        self.soft_assert(self.assertEqual, "Male", "Selected gender is not correct")
        self.soft_assert(self.assertEqual, "15 - 50", "Not in age group")
        self.soft_assert(self.assertTrue, driver.title.__contains__("Selenium Grid Online"))
        self.assert_all()

        driver.close()
