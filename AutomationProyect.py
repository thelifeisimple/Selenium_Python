from selenium import webdriver
import unittest
import time

busqueda = 'hola'
tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('hola mundo')
driver.find_element_by_name('submit_search').click()
time.sleep(2)
tc.assertEqual('No results were found for your search "hola mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p'))
driver.find_element_by_link_text('Women').click
time.sleep(2)
driver.find_elements_by_partial_link_text('res').click()
time.sleep(2)
driver.find_element_by_link_text('Casual Dresses').click()
#Partial_link_elemnet
driver.find_element_by_partial_link_text('Casual').click()
#class_name
driver.find_elements_by_name('subcategory-name').click()
#ccs_selector
driver.find_elements_by_css_selector('a.subcategory-name').click()

driver.close()
driver.quit()

