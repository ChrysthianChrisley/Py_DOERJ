# pip install msedge-selenium-tools

import requests, webbrowser
import base64
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

# URL da página
url = 'http://www.ioerj.com.br/portal/modules/conteudoonline/do_seleciona_edicao.php?data=MjAyMzA1MzE='

# Fazendo uma solicitação GET para a página
response = requests.get(url)

# Criando um objeto BeautifulSoup com o conteúdo HTML da página
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrando o elemento <a> com o link desejado
link = soup.find('a', text='Parte I (Poder Executivo)')

# Obtendo o valor do atributo href do elemento <a>
link_href = link['href']

# Imprimindo o link
print('Link:', link_href)

base64Link = link_href.split("session=")[1]

print('Base64:', base64Link)

decoded_string_1 = base64.b64decode(base64Link)
decoded_string_2 = base64.b64decode(decoded_string_1)
decoded_string_3 = base64.b64decode(decoded_string_2)

print('Código Final:', decoded_string_3)

openLink = "http://www.ioerj.com.br/portal/modules/conteudoonline/"+link_href

#webbrowser.open(openLink)


edgeBrowser = webdriver.Edge(r"msedgedriver.exe")

# URL da página onde está o botão de download
url = openLink

# Abrir a página no navegador

url2 = 'http://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?k='

edgeBrowser.get(url)

time.sleep(10)


# Localizar o botão de download pelo ID
botao_download = edgeBrowser.find_element(By.ID, 'viewFind')

# Clicar no botão de download
botao_download.click()

text_area = edgeBrowser.find_element_by_id('findInput')
text_area.send_keys("SEEDUC")

#edgeBrowser.switch_to.alert.accept()

#time.sleep(15)
# Fechar o navegador
#edgeBrowser.quit()
