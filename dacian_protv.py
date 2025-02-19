from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser with headless=False for visibility
    browser = p.chromium.launch(headless=False)  
    page = browser.new_page()
    
    # Navigate to the website
    page.goto("https://www.protv.ro/")

    # Click on the element for consent (using a CSS selector)
    page.click("#onetrust-accept-btn-handler")

    # Click on the element (using XPath)
    page.click('//HTML[1]/BODY[1]/MAIN[1]/SECTION[2]/DIV[1]/SECTION[1]/DIV[1]/DIV[1]/DIV[1]/ARTICLE[1]/DIV[1]/H3[1]/A[1]', 
               timeout=5000)  # Adjust timeout if needed

    # Navigate to the next page
    page.goto("https://www.protv.ro/articol/109120-noua-viata-a-lui-oscar-pistorius-la-12-ani-de-la-crima-care-a-socat-lumea-eliberat-din-inchisoare-fostul-atlet-paralimpic-traieste-intr-un-conac-luxos-si-se-iubeste-cu-sosia-celei-pe-care-a-ucis-o-in-2013-de-ziua-indragostitilor")
    
    # Close the browser
    browser.close()
