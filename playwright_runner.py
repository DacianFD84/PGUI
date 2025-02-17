from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Deschide browserul în fundal
        page = browser.new_page()
        page.goto("https://www.example.com")  # Navighează la o pagină

        page.screenshot(path="screenshot.png")  # Face captură de ecran
        print("Screenshot saved as 'screenshot.png'")  # Evită diacriticele

        browser.close()

run()
