from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho para o ChromeDriver
chrome_driver_path = "C:/Users/Lippe/Documents/projeto ispeed/chromedriver.exe"

# Configuração do ChromeDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Iniciar o navegador
driver = webdriver.Chrome(service=service, options=options)

try:
    # Acessar o perfil do Instagram
    driver.get('https://www.instagram.com/ispeedx/')

    # Esperar até que a página carregue completamente
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Procurar o link "gearup.onelink.me/Zmq0/ISPEEDX"
    link_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "gearup.onelink.me/Zmq0/ISPEEDX"))
    )
    link_element.click()

    # Esperar o redirecionamento e o carregamento da nova página
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Procurar o link específico para download
    download_button = WebDriverWait(driver, 5
                                    ).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='https://download.booster.gearupportal.com/9151/GearUP-2.3.0-win.exe?name=GearUP-2.3.0-brkol16.exe']"))
    )
    download_button.click()

    # Esperar o download começar (ajuste conforme necessário)
    time.sleep(1)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador
    driver.quit()