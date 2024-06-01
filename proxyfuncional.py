import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PROXY = '20.205.61.143:8123'
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://gearup.onelink.me/Zmq0/ISPEEDX')
time.sleep(100)