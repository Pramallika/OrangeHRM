from concurrent.futures import thread
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from Login_Page import login_Page

class test_orangeHRM(unittest.TestCase):
    def setUp(self):
        self.serv_obj = Service(r"C:\Users\SUBHAKAR\Documents\Prammu\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.login_Page = login_Page(self.driver)

    def test_login(self):
        self.login_Page.enter_username("Admin")
        self.login_Page.enter_password("admin123")
        self.login_Page.click_submit()
        time.sleep(2)

        try:
            current_url = self.driver.current_url
            expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            self.assertEqual(current_url,expected_url)
        except:
            expected_error_message = "Invalid credentials"
            error_message = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').text
            self.assertEqual(error_message,expected_error_message)
        
            
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
