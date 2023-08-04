from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        #definir primero todos nuestros elementos
        self.btnRegistrar = (By.NAME, "REGISTER")
        self.txtfirstName = (By.NAME, "firstName")
        self.txtlastName = (By.NAME, "lastName")
        self.txtphone = (By.NAME, "phone")
        self.txtuserName = (By.NAME, "userName")
        self.txtaddress1 = (By.NAME, "address1")
        self.txtcity = (By.NAME, "city")
        self.txtstate = (By.NAME, "state")
        self.txtpostalCode = (By.NAME, "postalCode")

        self.txtemail = (By.NAME, "email")
        self.txtpassword = (By.NAME, "password")
        self.txtconfirmPassword = (By.NAME, "confirmPassword")

        self.btnsubmit = (By.NAME, "submit")

        def enter_registration_details(self, first_name, last_name, phone, email, address, city, state, postal_code,country, username, password):
            self.driver.find_element(*self.txtFirstName).send_keys(first_name)
            self.driver.find_element(*self.txtLastName).send_keys(last_name)
            self.driver.find_element(*self.txtPhone).send_keys(phone)
            self.driver.find_element(*self.txtEmail).send_keys(email)
            self.driver.find_element(*self.txtAddress).send_keys(address)
            self.driver.find_element(*self.txtCity).send_keys(city)
            self.driver.find_element(*self.txtState).send_keys(state)
            self.driver.find_element(*self.txtPostalCode).send_keys(postal_code)
            self.driver.find_element(*self.txtCountry).send_keys(country)
            self.driver.find_element(*self.txtUsername).send_keys(username)
            self.driver.find_element(*self.txtPassword).send_keys(password)
            self.driver.find_element(*self.txtConfirmPassword).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*self.btnsubmit).click()
