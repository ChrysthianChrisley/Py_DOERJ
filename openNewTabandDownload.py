# pip install msedge-selenium-tools

import math
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium_1
from selenium.webdriver.support.ui import WebDriverWait



def new_tabDown():

    new_link = selenium_1.selenium_part1()

    #new_link = 'http://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?k=B22C7881-BACD7-4062-8FF5-A52F78C33BDC1'
    
    edgeBrowser = webdriver.Edge(r"msedgedriver.exe")

    edgeBrowser.get(new_link)
    time.sleep(3)

    edgeBrowser.maximize_window()

    window_width = edgeBrowser.execute_script("return window.innerWidth")
    window_height = edgeBrowser.execute_script("return window.innerHeight")

    center_x = math.floor(window_width / 4)
    center_y = math.floor(window_height / 4)

    actions = ActionChains(edgeBrowser)
    time.sleep(5)
    actions.move_by_offset(center_x, center_y).perform()
    actions.context_click().perform()

    time.sleep(1)
    # Localizar o primeiro item do menu
    
    wait = WebDriverWait(edgeBrowser, 10)
    
    actions.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()

    time.sleep(3)

    pyautogui.press("enter")

    time.sleep(2)
    edgeBrowser.quit()

#if __name__ == '__main__':
    #new_tabDown()
