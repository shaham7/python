from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Optional, for handling interactive elements

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com")

content_elements = driver.find_elements(By.ID, "content")
print(content_elements)

driver.quit()
