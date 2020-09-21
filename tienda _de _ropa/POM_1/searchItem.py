import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemPage = PageItems(self.driver)

    def test_search_no_elements(self):
        self.indexPage.search('hola')
        time.sleep(2)
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        #expected_result = 'No results were found for your search "Hola"'
        self.assertEqual(self.itemPage.return_no_element_text(), 'No results were found for your search "hola"')


    def test_search_find_dress(self):
        self.indexPage.search('dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemPage.return_section_titule())

    def test_search_find_tshirt(self):
        self.indexPage.search('t-shirts')
        time.sleep(2)
        self.assertTrue('T-SHIRTS' in self.itemPage.return_section_titule())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=='__main___':
    unittest.main()
