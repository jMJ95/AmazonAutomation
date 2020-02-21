"""HomePage """
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from project.locators.locators import Locators
from project.helpers import Helpers


class AmazonHomePage(Helpers):
    """Esta es la clase que contiene los elementos de la pagina de equipos de homepage"""

    def __init__(self, driver, test_name):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.test_name = test_name
        self.search = Locators.search_in
        self.search_btn = Locators.search_btn
        self.img_slider = Locators.img_slider
        self.search_select_dd = Locators.search_select_dd
        self.identifiquese_btn = Locators.identifiquese_drop_dowm

    def write_into_search_input(self, articulo:str):
        """
        Escribe artiulo en la barra de busqueda.
        """
        search = self.driver.find_element(by=self.search[0], value=self.search[1])
        search.clear()
        search.send_keys(articulo)

        self.driver.save_screenshot('./evidencias/' + self.test_name + '/write_search_input_' +
        self.getdatetime() + '.png')

    def click_search_btn(self):
        """
        Click en search_btn para buscar el articulo.
        """
        search_btn = self.driver.find_element(by=self.search_btn[0], value=self.search_btn[1])
        search_btn.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/click_search_btn_' +
        self.getdatetime() + '.png')

    def select_search_sel(self, tipo: str):
        """
        Selecciona el tipo de articulo.
        """
        select = Select(self.driver.find_element(by=self.search_select_dd[0], value=self.search_select_dd[1]))
        select.select_by_visible_text(tipo)
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/select_search_sel_' +
        self.getdatetime() + '.png')
    
    def click_img_slider(self):
        """
        clickea la imagen del slider.
        """
        img_slider = self.driver.find_element(by=self.img_slider[0], value=self.img_slider[1])
        print(img_slider.getAttribute("href"))
        # .click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/click_img_slider_' +
        self.getdatetime() + '.png')

    def click_identifiquese_btn(self):
        """
        clickea la pagina de identificación.
        """
        identifiquese_btn = self.driver.find_element(by=self.identifiquese_btn[0], value=self.identifiquese_btn[1])
        identifiquese_btn.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/identifiquese_btn_' +
        self.getdatetime() + '.png')
