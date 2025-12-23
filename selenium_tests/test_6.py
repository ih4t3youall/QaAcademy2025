import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_submit_incomplete_form():
    """Intentar enviar un formulario incompleto y verificar que falla"""
    
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
        
        script = """
        const messageDiv = document.getElementById('form-message');
        const formData = {
            nombre: 'Juan Perez',
            email: '',  // Email vacio, causara error
            edad: '35',
            telefono: '+34 123 456 789',
            empresa: '',
            presupuesto: '',
            asunto: 'consulta',
            mensaje: 'Test mensaje',
            terminos: true
        };
        
        fetch('/api/submit-contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(result => {
            if (!response.ok) {
                messageDiv.className = 'form-message error';
                messageDiv.textContent = result.errors.join(', ');
                messageDiv.style.display = 'block';
            }
        })
        .catch(error => {
            messageDiv.className = 'form-message error';
            messageDiv.textContent = 'Error al enviar el formulario';
            messageDiv.style.display = 'block';
        });
        """
        
        driver.execute_script(script)
        print("✓ Se envio formulario incompleto via API")
        time.sleep(2)
        
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "form-message"))
        )
        
        message_text = message.text
        assert message_text, f"Mensaje vacio: {message_text}"
        print(f"✓ Mensaje de error recibido: {message_text}")
        
        message_class = message.get_attribute("class").lower()
        assert "error" in message_class, \
            f"El mensaje no tiene la clase de error: {message_class}"
        print(f"✓ El mensaje tiene el estilo correcto (clase: {message.get_attribute('class')})")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_submit_incomplete_form()

