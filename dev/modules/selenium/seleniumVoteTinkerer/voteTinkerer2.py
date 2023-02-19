from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Sample test case started")  

#driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

print('Driver instantiated')

url = "https://www.python.org"
driver.get(url)

print(driver.title)

search_bar = driver.find_element(By.CLASS_NAME, "search-field")
search_bar.clear()
search_bar.send_keys("getting started with python")
sleep(3)
search_bar.send_keys(Keys.RETURN)

# returns the current url
print(driver.current_url)

# return the name of a new window which is launched
#print(driver.window_handles)

sleep(10)

driver.close()