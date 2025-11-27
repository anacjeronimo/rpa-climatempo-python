from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from openpyxl import Workbook

# CONFIGURAÇÕES
cidade = "São Paulo"

service = Service("chromedriver.exe")  # se estiver no PATH, pode só usar: Service()
driver = webdriver.Chrome(service=service)

# ACESSAR SITE
driver.get("https://www.climatempo.com.br/")
time.sleep(3)

# PESQUISAR CIDADE
barra = driver.find_element(By.ID, "search-input")
barra.send_keys(cidade)
time.sleep(1)
barra.send_keys(Keys.ENTER)
time.sleep(3)

# COLETAR TEMPERATURA
try:
    temperatura = driver.find_element(By.CSS_SELECTOR, ".-bold.-gray-dark-2._margin-r-5").text
except:
    temperatura = "Não encontrada"

# COLETAR CONDIÇÃO DO TEMPO
try:
    condicao = driver.find_element(By.CSS_SELECTOR, ".-gray._font-14._margin-l-5").text
except:
    condicao = "Não encontrada"

# FECHAR NAVEGADOR
driver.quit()

# SALVAR EM EXCEL
wb = Workbook()
ws = wb.active
ws.title = "Clima"

ws.append(["Cidade", "Temperatura", "Condição"])
ws.append([cidade, temperatura, condicao])

wb.save("previsao_tempo.xlsx")

print("Arquivo Excel gerado com sucesso!")
print(f"Cidade: {cidade}")
print(f"Temperatura: {temperatura}")
print(f"Condição: {condicao}")
