from dotenv import load_dotenv
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


load_dotenv()
password = os.environ.get("password")
email = os.environ.get("email")

options = Options()
options.add_argument("--window-size=1920x1080") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://clube.escolhatres.com.br/")
main_page = driver.current_window_handle
driver.find_element(By.XPATH, "//a[@class='p10 marrom s_light space2 upper button tcenter']").click()

for handle in driver.window_handles:
    if handle != main_page:
        print(handle)
        login_page = handle
        break

driver.switch_to.window(login_page)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block login-area-button']").click()
driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()

# for handle in driver.window_handles:
#     if handle != login_page:
#         print(handle)
#         main_page = handle
#         break
driver.switch_to.window(main_page)
# driver.get("https://clube.escolhatres.com.br/area-usuario")
print(driver.page_source)
sleep(10)
driver.find_element(By.XPATH, "//li[@class='margin']/a[@class='p12']").click()

sleep(3)
print(login_page)
print(main_page)

sleep(2)

