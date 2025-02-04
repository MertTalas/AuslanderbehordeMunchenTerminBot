import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import playsound  
import pyautogui

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL = "https://stadt.muenchen.de/service/info/unterabteilung-5-hochqualifizierte-und-sonderaufenthalte-kvr-ii-35/10338844/"

driver.get(URL)
driver.implicitly_wait(10)

def check_appointment():
    while True:
        driver.get(URL)
        time.sleep(2)

        try:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/article/div/div[1]/div/div/div/div/div[3]/div/a[1]"))
            )
            button.click()
            print("✅ Termin vereinbaren is clicked!")
        except:
            print("❌ Termin vereinbaren button could not be found...")
            continue

        try:
            pyautogui.moveTo(281, 887, duration=1)
            time.sleep(1)
            pyautogui.click()
            print("✅ Weiter zur Terminauswahl is clicked!")
        except:
            print("❌ Weiter zur Terminauswahl button could not be found...")
            continue
        
        elements = driver.find_elements(By.CSS_SELECTOR, "div.m-callout.m-callout--warning")
        if len(elements) > 0:
            print("❌ Termin not found, retrying...")  
            continue
        else:
            print("🟢 Termin found! Processing...")

            for _ in range(3):
                playsound.playsound("alarm.mp3")
                time.sleep(1)
            break

check_appointment()

driver.quit()
