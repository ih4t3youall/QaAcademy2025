"""
TEST 1: Verificar que la pagina HOME carga correctamente

Este es el test mas basico. Simplemente abre el navegador, accede a la URL
y verifica que el titulo de la pagina sea correcto.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_home_page_loads():
    """Verificar que la pagina home carga correctamente"""
    
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Descomenta para ejecutar sin GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Crear instancia del WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    # Configurar tiempos de espera
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(15)
    
    try:
        driver.get("http://localhost:8083/")
        time.sleep(2)  
        
        assert driver.title == "Home - Página Principal"
        print("✓ Test paso: La pagina home cargo correctamente")
        print(f"  Titulo: {driver.title}")
        time.sleep(1)
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_home_page_loads()



if __name__ == "__main__":
    test_home_page_loads()
