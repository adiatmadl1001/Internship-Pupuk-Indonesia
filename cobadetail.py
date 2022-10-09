from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/driver/chromedriver.exe')
driver.get('https://cpcl-frontend-dev-02-frzc53tfiq-et.a.run.app/auth/login')
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("admin@projecthanni.com")
driver.find_element(By.ID,"password").send_keys("123456"+Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/aside[1]/div[1]/ul[1]/li[11]/div[1]").click()
driver.find_element(By.LINK_TEXT,"User Management").click()
time.sleep(3)
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/div[1]/div[3]/button[1]").click()
time.sleep(2)
driver.save_screenshot("report/detail.png")
driver.find_element(By.XPATH,"//span[@class='ant-modal-close-x']").click()

driver.close()
driver.quit()