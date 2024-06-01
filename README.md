Bot criado para finalização de parcerias de visualizações ou donwloads altos demais

#estrutura de código abaixo

import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui 

#abrir o arquivo contendo vários proxies
with open("proxy_list.txt", "r") as file:
    proxy_list = file.readlines()
    proxy = random.choice(proxy_list).strip()

#adicionar o proxy 'modificado' do arquivo txt
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy}')

#caminho para o CHROMEDRIVER
driver = service = Service(executable_path=r"C:/Users/Lippe/Documents/projeto ispeed/chromedriver.exe") 
driver = webdriver.Chrome(service=service, options=chrome_options)

#tentativa para acessar o site determinado
#clique no botão "BAIXAR PARA Windows"
try:
        driver.get('https://gearup.onelink.me/Zmq0/ISPEEDX')
        WebDriverWait(driver, 10)
        download_button = WebDriverWait(driver, 7).until (
        )
except Exception as e:
    print(f'Erro Crítico: {e}')

time.sleep(50)
