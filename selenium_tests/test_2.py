import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_home_title_visible():
    """Verificar que el titulo principal de la pagina home es visible"""
    
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Descomenta para ejecutar sin GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(15)
    
    try:
        # Navegar a la URL
        driver.get("http://localhost:8083/")
        time.sleep(2)  
        
        title = driver.find_element(By.ID, "home-title")
        time.sleep(1)  
        
        assert title.is_displayed(), "El titulo no esta visible"
        
        assert "Bienvenido" in title.text, f"El texto no contiene 'Bienvenido': {title.text}"
        
        print("✓ Test paso: El titulo principal es visible")
        print(f"  Texto del titulo: {title.text}")
        time.sleep(1)
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_home_title_visible()
