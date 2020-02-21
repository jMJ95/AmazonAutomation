"""ArticleDetailsPage """
import sys, os, time
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from project.locators.locators import Locators
from project.helpers import Helpers


class ArticleDetailsPage(Helpers):
    """Esta es la clase que contiene los elementos de la pagina de equipos de articledetails"""

    def __init__(self, driver, test_name):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.test_name = test_name
        self.article_color = Locators.article_color

        
    def select_color(self, color: str):
        """
        Este selecciona el color del articulo.
        """
        article_color = self.driver.find_element(by=self.article_color[0], value=self.article_color[1]%(color))
        article_color.click()
        self.driver.save_screenshot('./evidencias/' + self.test_name + '/select_color_' +
        self.getdatetime() + '.png')

    

    