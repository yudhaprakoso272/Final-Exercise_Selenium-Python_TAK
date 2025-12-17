import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from Base import InitiateDriver
from Pages import LoginPage
from Library import read_config

class FiturLoginSaucedemoTest(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.browser = InitiateDriver.startBrowser()
        self.login_page = LoginPage(self.browser)
        self.username = read_config("Credentials", "username")
        self.password = read_config("Credentials", "password")
        driver = self.browser
        driver.find_element(By.CSS_SELECTOR,'[class="login_logo"]')
        driver.find_element(By.ID, "user-name")
        driver.find_element(By.ID, "password")
    
    def test_success_login(self):
        driver = self.browser
        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()
        
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()

        get_url = driver.current_url
        self.assertIn('/inventory.html', get_url)       

    def test_failed_login(self):
        driver = self.browser
        driver.find_element(By.ID, "user-name").send_keys("standard")
        driver.find_element(By.ID, "password").send_keys("secret")
        driver.find_element(By.ID, "login-button").click()

        error_message = driver.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Username and password do not match', error_message)

    def test_login_locked_out_user(self):
        driver = self.browser
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        error_message = driver.find_element(By.CSS_SELECTOR,'[data-test="error"]').text
        self.assertIn('Sorry, this user has been locked out', error_message)
         
    @classmethod
    def tearDown(self):
        InitiateDriver.closeBrowser()

if __name__ == '__main__':
    unittest.main(verbosity=2)