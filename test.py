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





time.sleep(2)

# # button : 0 reset, 1 capture all, 2 flip, 3 PGN?, 4 setting, 5 previous move, 6 nextmove
# #          7 calculate next move, 8 nextmove generated

setting_button = driver.find_elements(By.XPATH, '//*[@id="ncm-main"]/div/div[1]/div[1]/div[2]/div[3]/div/div[2]/div[2]/button')
setting_button[0].click()

format_checkbox = driver.find_elements(By.XPATH,'/html/body/div[9]/div/div/div[2]/div[3]/label/input')
format_checkbox[0].click()
# print(len(format_checkbox))

time.sleep(2)

close_setting_button = driver.find_element(By.XPATH,'//button[@class="p-2 -mx-2"]')
close_setting_button.click()

calculate_button = driver.find_elements(By.XPATH,"//button[text()='Calculate Next Move']")
calculate_button[0].click()    
print(len(calculate_button))

# print(setting_button)

# for i in setting_button :
#     i.click()


time.sleep(7)

driver.quit()


# print(len(setting_button))