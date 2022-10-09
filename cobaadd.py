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
driver.find_element(By.XPATH,"//span[normalize-space()='Tambah User']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='ant-btn ant-btn-secondary ant-btn-lg ant-btn-block']").click()
time.sleep(4)
driver.save_screenshot("report/Formtambah.png")
driver.find_element(By.ID,"fullName").send_keys("Adeeett")
driver.find_element(By.ID,"email").send_keys("adiatmalaksana3333@gmail.com")
driver.find_element(By.ID,"phone").send_keys("62818283637")
driver.find_element(By.ID,"gender").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Pria')]").click()
driver.find_element(By.ID,"role").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Surveyor')]").click()
driver.find_element(By.ID,"actived").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Non-Aktif')]").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='OK']").click()
time.sleep(5)
driver.save_screenshot("report/BerhasilTambah.png")



driver.close()
driver.quit()



