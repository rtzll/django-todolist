from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
import time


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()
driver.get("http://localhost:8000/auth/register/")
wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.ID, "id_username"))).send_keys("usuarioprueba")
wait.until(EC.element_to_be_clickable((By.ID, "id_email"))).send_keys("usuarioprueba@gmail.com")
wait.until(EC.element_to_be_clickable((By.ID, "id_password"))).send_keys("usuarioprueba")
wait.until(EC.element_to_be_clickable((By.ID, "id_password_confirmation"))).send_keys("usuarioprueba")
wait.until(EC.element_to_be_clickable((By.ID, "id_password_confirmation"))).submit()

wait.until(EC.element_to_be_clickable((By.ID, "id_username"))).send_keys("usuarioprueba")
wait.until(EC.element_to_be_clickable((By.ID, "id_password"))).send_keys("usuarioprueba")
wait.until(EC.element_to_be_clickable((By.ID, "id_password"))).submit()


wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).send_keys("Creando")
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).submit()

wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).send_keys("Lista")
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).submit()
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).send_keys("de")
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).submit()
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).send_keys("prueba")
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).submit()
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).send_keys("inicial")
wait.until(EC.element_to_be_clickable((By.ID, "id_description"))).submit()

wait.until(EC.element_to_be_clickable((By.ID, "checkbox"))).click()

time.sleep(10)