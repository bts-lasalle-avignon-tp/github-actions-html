import pytest
import os

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

def test_exemple():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #browser.implicitly_wait(0.5)

    fichierHTML = "/src/exemple1.html"
    browser.get('file://' + os.path.abspath(os.getcwd()) + fichierHTML) # load url

    assert browser.title == "Test HTML"

    texte_h1 = browser.find_element(By.TAG_NAME, "h1").text
    assert texte_h1 == "Exemples"