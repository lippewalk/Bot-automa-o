from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

# Get a list of proxies
req_proxy = RequestProxy()
proxies = req_proxy.get_proxy_list()

# Path to ChromeDriver
chrome_driver_path = "C:/Users/Lippe/Documents/projeto ispeed/chromedriver.exe"

# Loop through the proxy list and try each one
for proxy in proxies:
    try:
        ip_atual = proxy.get_address()
        pais_atual = proxy.country

        # Set up proxy in Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument(f'--proxy-server={ip_atual}')

        # Initialize the Chrome driver with the service and options
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        try:
            # Open the first link
            driver.get('https://www.instagram.com/ispeedx/')
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            #Acessar link UpGear
            link_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "encurtador.com.br/LU2LF"))
            )
            link_element.click()

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            #Encontrar e clicar no botão de instalação 
            pyautogui.click(552, 693, duration=5)

            #Esperar o download começar 
            time.sleep(5)  #Se necessário ajuste o tempo 

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        
        finally:
            driver.quit()

    except Exception as e:
        print(f"Erro ao configurar o proxy: {e}")