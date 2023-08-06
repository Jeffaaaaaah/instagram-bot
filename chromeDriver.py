from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as seExceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains 

def initChromeDriver(fullScreen=True, headLess=False, cookiesDirectory=None):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if fullScreen:
        options.add_argument("--window-size=1920,1080")
    if headLess:
        options.add_argument("--headless=new")
    if cookiesDirectory != None:
        options.add_argument(r"user-data-dir=" + cookiesDirectory)
        options.add_argument('lang=pt-br')

    return webdriver.Chrome(service=Service(), options=options)
