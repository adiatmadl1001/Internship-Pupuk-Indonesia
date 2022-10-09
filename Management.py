from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import HtmlTestRunner

class UserManagementTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/driver/chromedriver.exe')
        self.driver.get('https://cpcl-frontend-dev-02-frzc53tfiq-et.a.run.app/auth/login')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(By.ID,"email").send_keys("admin@projecthanni.com")
        self.driver.find_element(By.ID,"password").send_keys("123456"+Keys.ENTER)
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/aside[1]/div[1]/ul[1]/li[11]/div[1]").click()
        self.driver.find_element(By.LINK_TEXT,"User Management").click()

    def test_page(self):
        self.driver.find_element(By.XPATH,"//td[normalize-space()='1']")
        self.driver.save_screenshot("report/User Management/Page1.png")
        self.driver.find_element(By.LINK_TEXT,"2").click()
        self.driver.find_element(By.XPATH,"//td[normalize-space()='11']")
        self.driver.save_screenshot("report/User Management/Page2.png")
        self.driver.find_element(By.LINK_TEXT,"3").click()
        self.driver.find_element(By.XPATH,"//td[normalize-space()='21']")
        self.driver.save_screenshot("report/User Management/Page3.png")
        self.driver.find_element(By.LINK_TEXT,"4").click()
        self.driver.find_element(By.XPATH,"//td[normalize-space()='31']")
        self.driver.save_screenshot("report/User Management/Page4.png")
    
    def test_filter_urut(self):
        self.driver.save_screenshot("report/User Management/urut.png")
        self.driver.find_element(By.XPATH,"//span[@class='ant-table-cell-content']//div[@class='ant-table-column-sorters']").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/urut1.png")
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[3]/div[1]/span[1]/div[1]").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/urut2.png")
        self.driver.find_element(By.XPATH,"//div[@class='ant-table-column-sorters ant-tooltip-open']").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/urut3.png")
        self.driver.find_element(By.XPATH,"//th[@class='ant-table-cell ant-table-cell-fix-right ant-table-cell-fix-right-first ant-table-column-has-sorters']//div[@class='ant-table-column-sorters']").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/urut4.png")
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/thead[1]/tr[1]/th[5]/div[1]/span[1]/div[1]").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/urut5.png")

    def test_download(self):
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[2]/button[1]/a[1]").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/bukti download.png")

    def test_delete(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]").click()
        time.sleep(2)
        self.driver.save_screenshot("report/cek delete.png")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//span[normalize-space()='OK']")
        time.sleep(5)
        self.driver.save_screenshot("report/hasil delete.png")

    def test_edit(self):
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/div[1]/div[2]/button[1]/span[1]/*[name()='svg'][1]").click()
        self.driver.find_element(By.ID,"fullName").send_keys("TADI")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Cancel']").click()
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='OK']").click()

    def test_detail(self):
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/div[1]/div[3]/button[1]").click()
        time.sleep(2)
        self.driver.save_screenshot("report/User Management/detail.png")
        self.driver.find_element(By.XPATH,"//span[@class='ant-modal-close-x']").click()

    def test_add(self):
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Tambah User']").click()
        self.driver.find_element(By.CSS_SELECTOR,"button[class='ant-btn ant-btn-secondary ant-btn-lg ant-btn-block']").click()
        time.sleep(4)
        self.driver.save_screenshot("report/Formtambah.png")
        self.driver.find_element(By.ID,"fullName").send_keys("Adeeett")
        self.driver.find_element(By.ID,"email").send_keys("adiatmalaksana3333@gmail.com")
        self.driver.find_element(By.ID,"phone").send_keys("62818283637")
        self.driver.find_element(By.ID,"gender").click()
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Pria')]").click()
        self.driver.find_element(By.ID,"role").click()
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Surveyor')]").click()
        self.driver.find_element(By.ID,"actived").click()
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Non-Aktif')]").click()
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='OK']").click()
        time.sleep(5)
        self.driver.save_screenshot("report/User Management/BerhasilTambah.png")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/chromedriver_win32/report/User Management'))