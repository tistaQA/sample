from selenium import webdriver

driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()