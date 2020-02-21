"""Modulo de prueba de Busqueda de un producto"""

import sys, os, unittest, time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from selenium import webdriver
from project.pages.homepage import AmazonHomePage
from project.pages.articlespage import ArticlesPage
from project.pages.articledetailspage import ArticleDetailsPage
from project.helpers import Helpers

class TestSearchArticle(unittest.TestCase):
    """Prueba para buscar Articulo"""

    @classmethod
    def setUpClass(cls):
        cls.helpers = Helpers()
        cls.settings = cls.helpers.read_json_file('./settings.json')
        cls.tests = cls.helpers.read_json_file('./project/resources/data/tests.json')
        cls.insumos = cls.tests['search_article']
        cls.driver = webdriver.Chrome(executable_path=cls.settings['drivers']['chrome']['executable_path'])
        cls.driver.maximize_window()
        cls.driver.get(cls.settings['amazon'])

        cls.test_name = 'test_search_article'
        
        cls.home_page = AmazonHomePage(cls.driver, cls.test_name)
        cls.articles_page = ArticlesPage(cls.driver, cls.test_name)
        cls.article_d_page = ArticleDetailsPage(cls.driver, cls.test_name)

    def test_search_article(self):
        self.home_page.select_search_sel(self.insumos['departamento'])
        self.home_page.write_into_search_input(self.insumos['articulo'])
        self.home_page.click_search_btn()

        self.articles_page.select_art()
        self.article_d_page.select_color(self.insumos['color'])
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
