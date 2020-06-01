from selenium import webdriver
import unittest
import time

busqueda = 'hola'
tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')

driver.find_element_by_id('search_query_top').send_keys(busqueda)
driver.find_element_by_name('submit_search').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/p')
time.sleep(2)
tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text)

driver.close()
driver.quit()

