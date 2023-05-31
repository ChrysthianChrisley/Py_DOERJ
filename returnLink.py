# pip install msedge-selenium-tools

import requests, webbrowser
import base64
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import openNewTabandDownload as openNew
import encodeDate

def returnLink():

    data64 = encodeDate.encode()

    # URL da página
    url = 'http://www.ioerj.com.br/portal/modules/conteudoonline/do_seleciona_edicao.php?data='+data64

    # Fazendo uma solicitação GET para a página
    response = requests.get(url)

    # Criando um objeto BeautifulSoup com o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando o elemento <a> com o link desejado
    link = soup.find('a', text='Parte I (Poder Executivo)')

    # Obtendo o valor do atributo href do elemento <a>
    link_href = link['href']

    # Imprimindo o link
    #print('Link:', link_href)

    new_Link = "http://www.ioerj.com.br/portal/modules/conteudoonline/"+link_href

    return new_Link

