from playwright.sync_api import sync_playwright, expect
import time
from datetime import datetime

def test_recorded_script():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="recordings",
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        stepNumber = 1  # Initialize step counter
        
        try:
            print(f"Step {stepNumber}: Navigating to https://dacian.fyi/")
            page.goto("https://dacian.fyi/")
            page.wait_for_load_state("networkidle")
            print("Navigation successful")
            time.sleep(1)
            
            stepNumber += 1

            print(f"Step {stepNumber}: Clicking element")
            locator = page.locator("xpath=/html[1]/body[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]/a[1]")
            locator.wait_for(state="visible")
            locator.click()
            print("Click successful")
            time.sleep(1)
            
            stepNumber += 1

            print(f"Step {stepNumber}: Navigating to https://dacian.fyi/p/Cum-s%C4%83-Instalezi-%C8%99i-s%C4%83-configurezi-Ngrok")
            page.goto("https://dacian.fyi/p/Cum-s%C4%83-Instalezi-%C8%99i-s%C4%83-configurezi-Ngrok")
            page.wait_for_load_state("networkidle")
            print("Navigation successful")
            time.sleep(1)
            
            stepNumber += 1

            print(f"Step {stepNumber}: Clicking element")
            locator = page.locator("xpath=/html[1]/body[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/p[1]")
            locator.wait_for(state="visible")
            locator.click()
            print("Click successful")
            time.sleep(1)
            
            stepNumber += 1

            print(f"Step {stepNumber}: Double clicking element")
            locator = page.locator("xpath=/html[1]/body[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/p[1]")
            locator.wait_for(state="visible")
            locator.dblclick()
            print("Double click successful")
            time.sleep(1)
            
            stepNumber += 1

            print(f"Step {stepNumber}: Right clicking element")
            locator = page.locator("xpath=/html[1]/body[1]/div[3]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/p[1]")
            locator.wait_for(state="visible")
            locator.click(button="right")
            print("Right click successful")
            time.sleep(1)
            
            stepNumber += 1
            print("Test completed successfully")
        except Exception as e:
            print(f"Test failed: {str(e)}")
        finally:
            context.close()
            browser.close()
            print(f"Video recording saved in recordings/")

if __name__ == "__main__":
    test_recorded_script()