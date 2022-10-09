import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/driver/chromedriver.exe')
driver.get('https://cpcl-frontend-dev-02-frzc53tfiq-et.a.run.app/auth/login')
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("admin@projecthanni.com")
driver.find_element(By.ID,"password").send_keys("123456"+Keys.ENTER)
time.sleep(4)
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/aside[1]/div[1]/ul[1]/li[11]/div[1]").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"User Management").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[7]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]").click()
time.sleep(2)
driver.save_screenshot("report/cek delete.png")
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='OK']")
time.sleep(5)
driver.save_screenshot("report/hasil delete.png")

driver.close()
driver.quit()

