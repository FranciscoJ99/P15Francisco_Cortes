import unittest
from selenium import webdriver

from pom.registar_page import Registar_Page
from pom.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Instaciamos el webdriver
        self.driver = webdriver.Chrome()
        # Dirigirnos a la url
        self.driver.get("https://demo.guru99.com/test/newtours/")
        # Inicializamos la página de login

        self.login_page = LoginPage(self.driver)
        self.register_page = Registar_Page(self.driver)
        self.driver.implicitly_wait(20)

    def test_valid_registration(self):
        # Navegar a la página de registro
        self.login_page.click_register_link()

        # Ingresar detalles de registro válidos
        self.register_page.enter_registration_details("Francisco javier",
                                                      "Cortes Prieto",
                                                      "5511409542",
                                                      "pacojavier0599@gmail.com",
                                                      "Tultitlan",
                                                      "EDUMX",
                                                      "MX",
                                                      "54925",
                                                      "MEXICO",
                                                      "pacojavier",
                                                      "Ffrank")
        # Hacer clic en el botón de registro
        self.register_page.click_register_button()

        # Aquí puedes agregar aserciones para verificar que el registro fue exitoso.

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()