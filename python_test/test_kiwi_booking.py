import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FillForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_fill_rezervation_form(self):
        driver = self.driver
        #open kiwi home
        driver.get("http://kiwi.com")
        self.assertIn("Kiwi.com", driver.title)

        #remove default text - odkud
        driver.find_element_by_xpath("//*[@class='input-place-close']")

        #fill odkud
        odkud = driver.find_element_by_xpath("//*[@class='input-places-input input-origin']")
        odkud.send_keys("praha")
        odkud.send_keys(Keys.RETURN)
        assert "No result found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()

