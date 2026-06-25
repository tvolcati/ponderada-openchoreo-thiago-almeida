from pathlib import Path
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE = "http://openchoreo.localhost:8080/"
USER = "admin@openchoreo.dev"
PASSWORD = "Admin@123"
OUT = Path("docs/evidencias")
OUT.mkdir(parents=True, exist_ok=True)


def wait_one(driver, selectors, timeout=30, condition=EC.presence_of_element_located):
    wait = WebDriverWait(driver, timeout)
    last = None
    for by, value in selectors:
        try:
            return wait.until(condition((by, value)))
        except Exception as exc:
            last = exc
    raise last or TimeoutException("element not found")


options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1600,1200")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_page_load_timeout(60)
wait = WebDriverWait(driver, 30)

try:
    driver.get(BASE)
    time.sleep(3)
    driver.save_screenshot(str(OUT / "11-openchoreo-login-page.png"))
    (OUT / "11-openchoreo-login-page.html").write_text(driver.page_source, encoding="utf-8")

    sign_in = wait_one(driver, [
        (By.XPATH, "//button[contains(., 'Sign In') or contains(., 'Login') or contains(., 'Log in') or contains(., 'Entrar')]")
    ], condition=EC.element_to_be_clickable)
    sign_in.click()

    wait.until(lambda d: "thunder" in d.current_url or "auth" in d.current_url)
    time.sleep(3)
    driver.save_screenshot(str(OUT / "12-thunder-login-page.png"))
    (OUT / "12-thunder-login-page.html").write_text(driver.page_source, encoding="utf-8")

    username = wait_one(driver, [
        (By.CSS_SELECTOR, "input[name='username']"),
        (By.CSS_SELECTOR, "input[id='username']"),
        (By.CSS_SELECTOR, "input[type='email']"),
        (By.CSS_SELECTOR, "input[type='text']"),
    ])
    password = wait_one(driver, [
        (By.CSS_SELECTOR, "input[name='password']"),
        (By.CSS_SELECTOR, "input[id='password']"),
        (By.CSS_SELECTOR, "input[type='password']"),
    ])

    username.clear()
    username.send_keys(USER)
    password.clear()
    password.send_keys(PASSWORD)

    submit = wait_one(driver, [
        (By.CSS_SELECTOR, "button[type='submit']"),
        (By.CSS_SELECTOR, "input[type='submit']"),
        (By.XPATH, "//button[contains(., 'Sign In') or contains(., 'Login') or contains(., 'Log in') or contains(., 'Entrar')]")
    ], condition=EC.element_to_be_clickable)
    submit.click()

    wait.until(lambda d: "openchoreo.localhost:8080" in d.current_url and "thunder" not in d.current_url)
    time.sleep(8)
    driver.save_screenshot(str(OUT / "13-openchoreo-home.png"))
    (OUT / "13-openchoreo-home.html").write_text(driver.page_source, encoding="utf-8")
    print("OK")
    print(driver.current_url)
except Exception:
    driver.save_screenshot(str(OUT / "13-openchoreo-home-falha.png"))
    (OUT / "13-openchoreo-home-falha.html").write_text(driver.page_source, encoding="utf-8")
    raise
finally:
    driver.quit()
