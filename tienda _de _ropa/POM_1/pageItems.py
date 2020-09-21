class PageItems:

    def __init__(self, my_drive):
        self.not_result_banner = '//*[@id="center_column"]/p'
        self.titule_banner = '//*[@id="center_column"]/h1/span[1]'
        self.driver = my_drive

    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.not_result_banner).text

    def return_section_titule(self):
        return self.driver.find_element_by_xpath(self.titule_banner).text


