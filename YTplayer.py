from selenium import webdriver


chrome_driver_path = (r'C:\Users\Hatem Ben Gamra\Desktop\Math\\chromedriver.exe')
class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()


#assist = music()
#assist.play(vid)
