import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\david\\Documents\\selenium-python-sample\\driver\\chromedriver.exe')

    def test_login_valid_credentials(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        self.assertIn("Swag Labs", driver.title)

        user_name = "standard_user"
        password = "secret_sauce"

        user_name_field = driver.find_element_by_name("user-name")
        password_field = driver.find_element_by_name("password")
        login_btn = driver.find_element_by_id("login-button")

        time.sleep(1)
        user_name_field.send_keys(user_name)
        password_field.send_keys(password)
        time.sleep(1)
        login_btn.click()
        time.sleep(2)
        self.assertIn("inventory", driver.current_url)

    def test_login_invalid_credentials(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        self.assertIn("Swag Labs", driver.title)

        user_name = "standard_user"
        invalid_password = "invalid_password"

        user_name_field = driver.find_element_by_name("user-name")
        password_field = driver.find_element_by_name("password")

        time.sleep(1)
        user_name_field.send_keys(user_name)
        password_field.send_keys(invalid_password, Keys.ENTER)

        error_msg = driver.find_element_by_css_selector("[data-test='error']")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", error_msg.text)
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
