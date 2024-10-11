from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    
    radio_button = page.query_selector('//input[@value="FeMale"]')
    radio_button.click()
    
    check_boxes = page.query_selector_all('//input[@value="Cricket"] | //input[@value="Hockey"]')
    for check_box in check_boxes:
        if not check_box.is_checked():
            check_box.click()
    
    page.wait_for_timeout(3000)
    browser.close()