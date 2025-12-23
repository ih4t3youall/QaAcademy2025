"""
TEST 5: Enviar un formulario y verificar el resultado

Este test llena completamente el formulario de contacto, lo envia
y verifica que aparezca el mensaje de exito.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_submit_contact_form():
    """Llenar y enviar el formulario de contacto completo"""
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(15)
    
    try:
        driver.get("http://localhost:8083/contacto")
        time.sleep(2)
        print("✓ Pagina de contacto cargada")
        
        driver.find_element(By.ID, "nombre").send_keys("Juan Perez Garcia")
        time.sleep(0.4)
        driver.find_element(By.ID, "email").send_keys("juan.perez@example.com")
        time.sleep(0.4)
        driver.find_element(By.ID, "edad").send_keys("35")
        time.sleep(0.4)
        driver.find_element(By.ID, "telefono").send_keys("+34 123 456 789")
        time.sleep(0.4)
        driver.find_element(By.ID, "empresa").send_keys("Tech Solutions S.A.")
        time.sleep(0.4)
        driver.find_element(By.ID, "presupuesto").send_keys("10000")
        time.sleep(0.4)
        
        select = Select(driver.find_element(By.ID, "asunto"))
        select.select_by_value("consulta")
        time.sleep(0.5)
        
        driver.find_element(By.ID, "mensaje").send_keys(
            "Hola, me gustaria consultar sobre vuestros servicios."
        )
        time.sleep(0.5)
        
        driver.find_element(By.ID, "terminos").click()
        time.sleep(0.5)
        print("✓ Formulario completado")
        time.sleep(1)
        
        submit_button = driver.find_element(By.ID, "submit-btn")
        submit_button.click()
        print("✓ Formulario enviado")
        time.sleep(2)
        
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "form-message"))
        )
        
        assert "correctamente" in message.text.lower(), f"Mensaje inesperado: {message.text}"
        print(f"✓ Mensaje de exito recibido: {message.text}")
        
        assert "success" in message.get_attribute("class"), "El mensaje no tiene la clase 'success'"
        print("✓ El mensaje tiene el estilo correcto (clase success)")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_submit_contact_form()
