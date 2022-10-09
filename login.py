import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/driver/chromedriver.exe')
        self.driver.get('https://cpcl-frontend-dev-02-frzc53tfiq-et.a.run.app/auth/login')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def test_login_valid(self):
        self.driver.find_element(By.ID,"email").send_keys("admin@projecthanni.com")
        self.driver.find_element(By.ID,"password").send_keys("123456" + Keys.ENTER)
        time.sleep(3)
        self.driver.save_screenshot("report/Login Test/Dashboard.png")
        self.driver.find_element(By.CLASS_NAME,"ant-dropdown-trigger").click()
        self.driver.find_element(By.LINK_TEXT,"Logout").click()

    def test_login_invalid(self):
        self.driver.find_element(By.ID,"email").send_keys("admin@projecthanni.com")
        self.driver.find_element(By.ID,"password").send_keys("1234567" + Keys.ENTER)
        errmssg= self.driver.find_element(By.CLASS_NAME,"ant-message").is_enabled()
        self.driver.save_screenshot("report/Login Test/Error.png")
        print(errmssg)
        
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/chromedriver_win32/report/Login Test'))