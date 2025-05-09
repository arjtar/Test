from selenium import webdriver
driver = webdriver.Chrome("C:\testdrive\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element_by_name("txtusername").send_keys("tomsmith")
driver.find_element_by_id("txtPassword").send_keys("SuperSecretPassword!")


