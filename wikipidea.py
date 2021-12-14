from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = (r'C:\Users\Hatem Ben Gamra\Desktop\Math\\chromedriver.exe')

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()

    assist = infow()
    assist.get_infow(information)