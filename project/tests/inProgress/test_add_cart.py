""" Modulo de prueba de Busqueda de un producto"""

import sys, os, unittest, time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium import webdriver

from project.helpers import Helpers
from project.tests.test_search_article import TestSearchArticle

class TestAddCart(unittest.TestCase):
    """Prueba de agregar al carrito"""

    @classmethod
    def setUpClass(cls):
        cls.helpers = Helpers()
        cls.settings = cls.helpers.read_json_file('./settings.json')
        cls.tests = cls.helpers.read_json_file('./project/resources/data/tests.json')
        cls.insumos = cls.tests['AddCart']
        cls.driver = webdriver.Chrome(executable_path=cls.settings['drivers']['chrome']['executable_path'])
        cls.driver.maximize_window()
        cls.driver.get(cls.settings['amazon'])

        cls.test_name = 'TestAddCart'

    def test_agregar_metodos_pago(self):
        TestSearchArticle()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
