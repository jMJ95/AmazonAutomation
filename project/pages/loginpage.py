"""RegistroPage """
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from project.locators.locators import Locators
from project.helpers import Helpers


class RegistroPage(Helpers):
    """Esta es la clase que contiene los elementos de la pagina de equipos de homepage"""

    def __init__(self, driver, test_name):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.test_name = test_name
        self.registro_btn = Locators.registro_btn
        self.input_in_reg = Locators.input_registro
        self.cont = Locators.continue_btn
        
        
    def click_registro_btn(self):
        """
        clickea el botón crea una cuenta de amazon.
        """
        registro_btn = self.driver.find_element(by=self.registro_btn[0], value=self.registro_btn[1])
        registro_btn.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/registro_btn_' +
        self.getdatetime() + '.png')

    def write_in_input_registro(self, nombre: str, correo: str, passwd: str):
        """
        llenar los datos de registro.
        """
        name = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%('Tu nombre')) 
        name.send_keys(nombre)
        email = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%('Correo electrónico'))
        email.send_keys(correo)
        psswd = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%('Contraseña'))
        psswd.send_keys(passwd)
        repeat_psswd = self.driver.find_element(by=self.input_in_reg[0], value=self.input_in_reg[1]%('Vuelve a escribir la contraseña'))
        repeat_psswd.send_keys(passwd)

        self.driver.save_screenshot('./evidencias/' + self.test_name + '/write_in_input_registro_' +
        self.getdatetime() + '.png')

    def click_registrar_btn(self):
        """
        Click en el boton registrar.
        """
        self.driver.find_element(by=self.cont[0], value=self.cont[1]).click()

        self.driver.save_screenshot('./evidencias/' + self.test_name + '/write_in_input_registro_' +
        self.getdatetime() + '.png')
