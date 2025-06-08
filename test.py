from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='2.0/chromedriver.exe')
driver = webdriver.Chrome(service=service)

classname = 'inline-block w-[1rem] h-[1rem] pb-[0.1rem] link'

driver.get(r'https://nextchessmove.com//?fen=rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR%20w%20KQkq%20-%200%201')



# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,classname)))

driver.find_element(By.XPATH,"//button[text()='Calculate Next Move']")

calculate_button = driver.find_element(By.XPATH,"//button[text()='Calculate Next Move']")
    
# # button : 0 reset, 1 capture all, 2 flip, 3 PGN?, 4 setting, 5 previous move, 6 nextmove
# #          7 calculate next move, 8 nextmove generated
calculate_button.click()

time.sleep(7)

# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[class()='link']")))
elements = driver.find_elements(By.XPATH,"//button[@class='link']")
print(elements[0].text)

# link = driver.find_element(By.ID,'mt-4 w-[612px]')
# # link.click()
# print(link)

# input_elements = driver.find_element(By.CLASS_NAME,classname)
# # input_element.clear()  #if something on the way
# input_element.send_keys('test'+Keys.ENTER)



time.sleep(5)

driver.quit()