# pip install msedge-selenium-tools
# pip install pdfkit
# pip install pyautogui

import requests, webbrowser
import base64
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import openNewTabandDownload as openNew
import returnLink

def selenium_part1():
    
    new_link = returnLink.returnLink()

    edgeBrowser = webdriver.Edge(r"msedgedriver.exe")

    # URL da página onde está o botão de download
    url = new_link

    # Abrir a página no navegador
    edgeBrowser.get(url)

    time.sleep(5)

    # Localizar o botão de download pelo ID
    botao_Buscar = edgeBrowser.find_element(By.ID, 'viewFind')

    # Clicar no botão de download
    botao_Buscar.click()

    text_area = edgeBrowser.find_element_by_id('findInput')
    text_area.send_keys("Ciência,  Tecnologia  e  Inovação")

    time.sleep(5)

    # Localizar o botão de download pelo ID
    botao_Avancar = edgeBrowser.find_element(By.ID, 'findNext')

    # Clicar no botão de download
    botao_Avancar.click()
    botao_Avancar.click()

    # Localizar o botão de download pelo ID
    botao_Download = edgeBrowser.find_element(By.ID, 'download')

    # Clicar no botão de download
    botao_Download.click()

    edgeBrowser.switch_to.alert.accept()
    time.sleep(2)

    
    edgeBrowser.switch_to.window(edgeBrowser.window_handles[1])
    new_url = edgeBrowser.current_url
    
    
    edgeBrowser.quit()
    time.sleep(2)

    return new_url

#window_name = edgeBrowser.window_handles[0]
#edgeBrowser.switch_to.window(window_name=window_name)


#time.sleep(5)
#edgeBrowser.get(new_url)

#openNew.new_tabDown(new_url)

#botao_Salvar = edgeBrowser.find_element(By.ID, 'save')
#botao_Salvar.click()

#edgeBrowser.switch_to.alert.accept()

#time.sleep(15)
# Fechar o navegador
#edgeBrowser.quit()


