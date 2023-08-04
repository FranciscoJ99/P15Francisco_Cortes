import unittest
from selenium import webdriver

from pom.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        #instaciamos el webdriver
        self.driver = webdriver.Chrome()
        #dirigirnos a la url
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.login_page = LoginPage(self.driver)
        self.driver.implicitly_wait(20)

    def test_login_without_credentials(self):
        # Intentar hacer inicio de sesión sin ingresar datos
        self.login_page.clickbtnSubmit()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()