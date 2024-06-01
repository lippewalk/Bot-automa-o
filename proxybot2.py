import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
PROXY = '20.206.106.192:8123'
chrome_options = webdriver.ChromeOptions
chrome_options.add_argument=(f'--proxy-server={PROXY}')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get('https://www.myip.com/')
time.sleep(100)