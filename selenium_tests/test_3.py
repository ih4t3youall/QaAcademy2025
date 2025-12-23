
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_click_contact_button():
    """Verificar que hacer clic en el boton de contacto navega correctamente"""
    
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
        driver.get("http://localhost:8083/")
        time.sleep(2)
        print(f"URL actual: {driver.current_url}")
        
        contact_button = driver.find_element(By.ID, "contact-button")
        time.sleep(1)
        print(f"✓ Boton encontrado: {contact_button.text}")
        
        assert contact_button.is_displayed(), "El boton no esta visible"
        print("✓ El boton es visible")
        time.sleep(1)
        
        contact_button.click()
        print("✓ Se hizo clic en el boton")
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "contact-title"))
        )
        print("✓ La pagina de contacto cargo")
        
        assert "contacto" in driver.current_url.lower(), f"URL no contiene 'contacto': {driver.current_url}"
        print(f"✓ Navegacion exitosa a: {driver.current_url}")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_click_contact_button()
