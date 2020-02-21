"""Modulo de prueba de comprobacion de un ubicacion"""

import sys, os, unittest, time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from project.pages.homepage import AmazonHomePage
from project.pages.checklocationpage import CheckLocationPage
from project.helpers import Helpers

class TestCheckLocation(unittest.TestCase):
    """Metodo para comprobar ubicacion"""

    @classmethod
    def setUpClass(cls):
        cls.helpers = Helpers()
        cls.settings = cls.helpers.read_json_file('./settings.json')
        cls.tests = cls.helpers.read_json_file('./project/resources/data/tests.json')
        cls.insumos = cls.tests['check_location']
        cls.driver = webdriver.Chrome(executable_path=cls.settings['drivers']['chrome']['executable_path'])
        cls.driver.maximize_window()
        cls.driver.get(cls.settings['amazon'])

        cls.test_name = 'test_check_location'
        
        cls.home_page = AmazonHomePage(cls.driver, cls.test_name)
        cls.check_location_page = CheckLocationPage(cls.driver, cls.test_name)
        
    def test_check_location(self):
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.home_page.click_img_slider()
        self.check_location_page.click_location_page_btn(self.insumos['btn_location_page'])
        self.check_location_page.check_location(self.insumos['pais'])


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
