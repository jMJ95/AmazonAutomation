"""Modulo de prueba de Registro correo de prueba"""

import sys, os, unittest, time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from project.pages.homepage import AmazonHomePage
from project.pages.loginpage import RegistroPage
from project.helpers import Helpers

class TestRegistroCorreodePrueba(unittest.TestCase):
    """Metodo para comprobar ubicacion"""

    @classmethod
    def setUpClass(cls):
        cls.helpers = Helpers()
        cls.settings = cls.helpers.read_json_file('./settings.json')
        cls.tests = cls.helpers.read_json_file('./project/resources/data/tests.json')
        cls.usuarios = cls.helpers.read_json_file('./project/resources/data/usuarios.json')
        cls.insumos = cls.tests['registro_correo_de_prueba']
        cls.usuario = cls.usuarios['usuario']
        cls.driver = webdriver.Chrome(executable_path=cls.settings['drivers']['chrome']['executable_path'])
        cls.driver.maximize_window()
        cls.driver.get(cls.settings['amazon'])

        cls.test_name = 'test_registro_correo_de_prueba'
        
        cls.home_page = AmazonHomePage(cls.driver, cls.test_name)
        cls.login_page = RegistroPage(cls.driver, cls.test_name)
        
    def test_registro_correo_de_prueba(self):
        self.home_page.click_identifiquese_btn()
        self.login_page.click_registro_btn()
        self.login_page.write_in_input_registro(self.usuario['nombre'],
                                    self.usuario['correo'],
                                    self.usuario['passwd'])
        self.login_page.click_registrar_btn()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
