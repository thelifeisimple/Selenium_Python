import unittest
from selenium import webdriver
import time
from pageIndexHW import PageIndexHW
from pageItemsHW import PageItemsHW
from pageItemHW import PageItemHW

# Sitio: http://automationpractice.com/index.php

# 1-Buscar por T-shirts
# 2-Al elemento que aparece, le clickean el color naranja
# 3-Poner 25 en cantidad
# 4-Clickear 3 veces el boton +
# 5-Verificar que el numero que aparece es 28


class homework_5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        # wait implicit
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndexHW(self.driver)
        self.itemsPage = PageItemsHW(self.driver)
        self.itemPage = PageItemHW(self.driver)

    @unittest.skip("Not needed now")
    def test_search_element(self):
        self.indexPage.search('T-shirt')
        #wait explicit
        time.sleep(2)
        self.assertTrue("T-SHIRT" in self.itemsPage.return_section_titule())

    def test_tarea(self):
        #21.567s
        self.indexPage.search('T-shirt')
        #wait implicit
        time.sleep(2)
        self.itemsPage.click_orange_button()
        self.itemPage.enter_quantity('25')
        self.itemPage.add_elements(3)
        number = self.itemPage.get_number_of_elements()
        self.assertTrue(number == '28')

    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_by_text('Product Name: A to Z')
        time.sleep(3)
        self.itemsPage.select_by_value('reference:asc')
        time.sleep(3)
        self.itemsPage.select_by_index(3)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




