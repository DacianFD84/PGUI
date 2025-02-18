from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Lansați browserul
    browser = p.chromium.launch()
    page = browser.new_page()

    # Navigați pe site
    page.goto("https://dacian.fyi/")

    # Click pe element
    page.click(".fs-16.text-black.fw-6")

    # Navigați la o altă pagină
    page.goto("https://dacian.fyi/p/Introducere-%C3%AEn-Mermaid-%C8%99i-utilizarea-sa-%C3%AEn-draw-io")

    # Închideți browserul
    browser.close()
