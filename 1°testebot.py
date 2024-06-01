import time
from isort import file
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui 

with open("proxy_list.txt", "r") as file:
    proxy_list = file.readlines()
    proxy = proxy_list[0].strip()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy}')

driver = service = Service(executable_path=r"C:/Users/Lippe/Documents/projeto ispeed/chromedriver.exe") 
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
        driver.get('https://gearup.onelink.me/Zmq0/ISPEEDX')
        WebDriverWait(driver, 10)
        download_button = WebDriverWait(driver, 7).until (
            pyautogui.click(552,693, duration=5)
        )
except Exception as e:
    print(f'Erro Crítico')

time.sleep(100)

