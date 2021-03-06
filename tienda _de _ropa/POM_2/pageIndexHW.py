from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageIndexHW:

    def __init__(self, my_driver):
        # Use BYs
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        # Use find_elements
        #self.query_top = 'search_query_top'
        #self.query_button = 'submit_search'
        self.driver = my_driver

    def search(self, item):

        search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
        search_box.send_keys(item)
        search_button = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.query_button))
        search_button.click()



        # Use BYs
        #self.driver.find_element(*self.query_top).send_keys(item)
        #self.driver.find_element(*self.query_button).click()
        #Use find_elements
        #self.driver.find_element_by_id(self.query_top).send_keys(item)
        #self.driver.find_element_by_name(self.query_button).click()

