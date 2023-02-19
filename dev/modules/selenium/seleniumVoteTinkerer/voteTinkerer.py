from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Sample test case started")  

#driver = webdriver.Chrome()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Firefox()  
#driver = webdriver.ie()  

driver.maximize_window()  
#navigate to the url  
url = "https://www.google.com/"
driver.get(url)

#sleep(5)
#driver.find_element_by_id("L2AGLb").send_keys(Keys.ENTER) 

#identify the Google search text box and enter the value  

driver.find_element_by_name("q").send_keys("gerbil")
sleep(3)

#click on the Google search button  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
sleep(3)
driver.close()  
print("Sample test case successfully completed")  