from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\testdrive\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()