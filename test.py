from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='2.0/chromedriver.exe')
driver = webdriver.Chrome(service=service)

classname = 'inline-block w-[1rem] h-[1rem] pb-[0.1rem] link'

driver.get('https://nextchessmove.com/')

# html = driver.page_source
# print(html[:1000])

# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,classname)))

elements = driver.find_elements(By.XPATH,"//*")
for ele in elements :
    print(f"Tag : {ele.tag_name}, Class : {ele.get_attribute('class')}")

# link = driver.find_element(By.CLASS_NAME,classname)
# link.click()

# input_element = driver.find_element(By.CLASS_NAME,classname)
# input_element.clear()  #if something on the way
# input_element.send_keys('test'+Keys.ENTER)



time.sleep(5)

driver.quit()