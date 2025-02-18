from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Deschide browserul în fundal
        page = browser.new_page()

        # Navighează pe Google
        page.goto("https://www.google.com")

        # Găsește câmpul de căutare și trimite o interogare
        search_box = page.locator("input[name='q']")
        search_box.fill("Playwright Python")  # Căutare "Playwright Python"
        search_box.press("Enter")

        # Așteaptă ca rezultatele să fie încărcate
        page.wait_for_selector("h3")

        # Extrage primele titluri de pe pagină
        results = page.locator("h3")
        for result in results.all_text_contents():
            print(result)

        # Închide browserul
        browser.close()

run()