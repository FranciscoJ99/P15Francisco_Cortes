
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        #definir priemro nuestros elementos
        self.txtUsername = (By.NAME, "userName")
        self.txtPass = (By.NAME, "password")
        self.btnSubmit = (By.NAME, "submit")
        self.lnkRegister = (By.LINK_TEXT, "REGISTER")

        #Definición de las acciones para los elementos
    def writeName (self, username):
        self.driver.find_element(*self.txtUsername).send_keys(username)

    def writePassword (self, password):
        self.driver.find_element(*self.txtPass).send_keys(password)

    def clickbtnSubmit(self):
        self.driver.find_element(*self.btnSubmit).click()

    def click_register_link(self):  # Método para hacer clic en el enlace de registro
        self.driver.find_element(*self.lnkRegister).click()
