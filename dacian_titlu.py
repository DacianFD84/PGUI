from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Deschide browserul vizibil
        page = browser.new_page()

        # Navighează la o pagină web
        page.goto("https://example.com")

        # Extrage titlul paginii
        title = page.title()
        print(f"Titlul paginii este: {title}")

        # Închide browserul
        browser.close()

run()
