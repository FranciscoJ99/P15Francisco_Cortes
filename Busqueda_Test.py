#Libreria
import selenium
from selenium import webdriver

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

#instanciar un webdriver
driver = webdriver.Chrome()

#Inicializar el navegador
driver.get('https://demo.guru99.com/test/newtours/')

try:

    #localizar el username
    txtUsername = driver.find_element(By.NAME, 'userName')
    # localizar el password
    txtpassword = driver.find_element(By.NAME, 'password')
    # localizar el boton de submit
    btnSubmit = driver.find_element(By.NAME, 'submit')

    #escribir en el nombre
    txtUsername.send_keys("user1")
    # escribir en el nombre
    txtpassword.send_keys("password1")
    #hacer click en submit
    btnSubmit.click()
    #espera implicita
    driver.implicitly_wait(20)
    #obtener el titulo de la pagina
    tituloPagina = driver.title
    #hacer una validacion
    assert tituloPagina == "Login: Mercury Tours"

except NoSuchElementException:
    print("No se puede encontrar el elemento")

finally:
    #cerramos el navegador
    print("Termina el test")
    #driver.quit()