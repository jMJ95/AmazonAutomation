"""CheckLocation"""

import sys, os, unittest, time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from project.locators.locators import Locators
from project.helpers import Helpers

class CheckLocationPage(unittest.TestCase):
    """confirmar a que zona pertenece tu pais"""
    def __init__(self, driver, test_name):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.test_name = test_name
        self.location_page_btn = Locators.location_page_btn

    def click_location_page_btn(self, texto: str):
        """
        clickea el boton que desees.
        """
        location_page_btn = self.driver.find_element(by=self.location_page_btn[0], value=self.location_page_btn[1])
        location_page_btn.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/click_location_page_btn' +
        self.getdatetime() + '.png')

    def check_location(self, pais:  str):

        for counter in range(0,4):
            table = self.driver.find_element(by=self.table[0], value=self.table[1]%(counter))
            if pais in table:
                print(counter)

