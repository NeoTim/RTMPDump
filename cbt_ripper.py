from selenium import webdriver
import unittest
import time
import os


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = os.environ["target"]
        self.login_url = "https://www.cbtnuggets.com/login"
        self.password = os.environ["password"]
        self.username = os.environ["username"]
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        # login!
        driver = self.driver
        driver.get(self.login_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_id("passwordPass").clear()
        driver.find_element_by_id("passwordPass").send_keys(self.password)
        driver.find_element_by_id("LoginAction").click()
        self.driver.implicitly_wait(12)  # slow internet here ;(

        # do stuff
        driver = self.driver
        driver.get(self.base_url)

        links = driver.find_elements_by_xpath("//a[@class='video_title']")
        urls = []

        for index, link in enumerate(links):
            u = link.get_attribute("href")
            title = "%s - %s" % (index, link.text)
            print title
            urls.append(u)

        for url in urls:
            driver.get(url)
            time.sleep(16)  # bad bad internet ;(

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
