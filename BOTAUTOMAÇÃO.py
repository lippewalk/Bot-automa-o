from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

#chrome driver para inicio do código
chrome_driver_path = "C:/Users/Lippe/Documents/projeto ispeed/chromedriver.exe"

#Config para execução 
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

#Iniciar o navegador 
driver = webdriver.Chrome(service=service, options=options)

try:
    #primeiro link 
    driver.get('https://www.instagram.com/ispeedx/')

    #tempo de espera 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    #acessa o link para a upGear 
    link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "         "))
    )
    link_element.click()

    #tempo de espera
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    #procurar o link de download
    download_button = WebDriverWait(driver, 7).until (
        pyautogui.click(552,693, duration=5)
    )
                                                       

    #esperar o download começar
    time.sleep(5)  # Ajuste o tempo conforme necessário

except Exception as e:
    print(f"Ocorreu um erro: {e}")
 


