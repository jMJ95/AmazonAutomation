"""ArticlePage """
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from project.locators.locators import Locators
from project.helpers import Helpers


class ArticlesPage(Helpers):
    """Esta es la clase que contiene los elementos de la pagina de equipos de homepage"""

    def __init__(self, driver, test_name):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.test_name = test_name
        self.article = Locators.article
        
    def select_art(self):
        """
        Este selecciona el articulo de la lista.
        """
        article = self.driver.find_element(by=self.article[0], value=self.article[1])
        article.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/select_art_' +
        self.getdatetime() + '.png')

    

    