from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Lansați browserul cu opțiunea headless=False pentru a-l vedea
    browser = p.chromium.launch(headless=False)  # Setează headless=False pentru vizibilitate
    page = browser.new_page()
    
    # Navigați pe site
    page.goto("https://dacian.fyi/")

    # Click pe butonul de login
    page.click(".fs-14.text-primary.fw-6.login-btn.d-none.d-sm-block")

    # Completați câmpul email
    page.fill("#formInputEmail", "dacian@florindedu.ro")

    # Completați câmpul parolă
    page.fill("#formInputPassword", "Phcops7666@")

    # Bifați checkbox-ul
    page.check("#formCheck")

    # Click pe butonul de login
    page.click(".btn.btn-primary")

    # Navigați pe pagina de login
    page.goto("https://dacian.fyi/login")

    # Închideți browserul
    browser.close()
