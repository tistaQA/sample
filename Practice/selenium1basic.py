from selenium import webdriver


driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")

driver.get("https://google.com/")
#driver.refresh()
driver.close()

