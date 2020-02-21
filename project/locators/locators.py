"""Importar paquetes de Selenium.
 Modulo de localizadores"""
from selenium.webdriver.common.by import By

class Locators:
    """
    En esta clase se encuentran los localizadores de los elementos
    """
    # * Elementos de la pagina principal
    search_in = (By.XPATH, '//div[@class="nav-fill"]/div[@class="nav-search-field "]/input')
    search_btn = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')
    search_select_dd = (By.XPATH, '//*[@id="searchDropdownBox"]')
    img_slider = (By.XPATH, '//*[@id="8e53VJp_VYQ-MhfMqwm8KA"]/div/div/span/a')
    identifiquese_drop_dowm = (By.XPATH, '//*[@id="nav-link-accountList"]/span[2]')


    # * Elementos del catalogo
    article = (By.XPATH, '//*[@class="s-include-content-margin s-border-bottom"]/div/div[2]/div[1]')
    article_color = (By.XPATH, '//div[@id="variation_color_name"]/ul/li[contains(@title,"%s")]')

    # * Elementos de pagina de ubicacion
    location_page_btn = (By.XPATH, '//*[@class="align-start"]/a[contains(text(), "%s")]')
    table =(By.XPATH, '//div[@class="help-content"]/div/table[%d]')

    # * Elementos de Login Page
    registro_btn = (By.XPATH, '//*[@id="createAccountSubmit"]')
    input_registro = (By.XPATH, '//*[@class="a-row a-spacing-base" and ./label[contains(text(),"%s")]]/input')
    continue_btn = (By.XPATH, '//*[@id="continue"]')