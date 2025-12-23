import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_fill_contact_form():
    """Llenar el formulario de contacto con datos completos"""
    
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
        
        nombre_field = driver.find_element(By.ID, "nombre")
        nombre_field.send_keys("Juan Perez Garcia")
        time.sleep(0.5)
        print("✓ Campo nombre completado")
        
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("juan.perez@example.com")
        time.sleep(0.5)
        print("✓ Campo email completado")
        
        edad_field = driver.find_element(By.ID, "edad")
        edad_field.send_keys("35")
        time.sleep(0.5)
        print("✓ Campo edad completado")
        
        telefono_field = driver.find_element(By.ID, "telefono")
        telefono_field.send_keys("+34 123 456 789")
        time.sleep(0.5)
        print("✓ Campo telefono completado")
        
        empresa_field = driver.find_element(By.ID, "empresa")
        empresa_field.send_keys("Tech Solutions S.A.")
        time.sleep(0.5)
        print("✓ Campo empresa completado")
        
        presupuesto_field = driver.find_element(By.ID, "presupuesto")
        presupuesto_field.send_keys("10000")
        time.sleep(0.5)
        print("✓ Campo presupuesto completado")
        
        select_asunto = Select(driver.find_element(By.ID, "asunto"))
        select_asunto.select_by_value("consulta")
        time.sleep(0.5)
        print("✓ Opcion de asunto seleccionada")
        
        mensaje_field = driver.find_element(By.ID, "mensaje")
        mensaje_field.send_keys("Hola, me gustaria consultar sobre vuestros servicios.")
        time.sleep(0.5)
        print("✓ Campo mensaje completado")
        
        terminos_checkbox = driver.find_element(By.ID, "terminos")
        terminos_checkbox.click()
        time.sleep(0.5)
        assert terminos_checkbox.is_selected(), "El checkbox no esta marcado"
        print("✓ Terminos aceptados")
        
        assert nombre_field.get_attribute("value") == "Juan Perez Garcia"
        assert email_field.get_attribute("value") == "juan.perez@example.com"
        assert edad_field.get_attribute("value") == "35"
        print("✓ Todos los datos se ingresaron correctamente")
        time.sleep(1)
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_fill_contact_form()
