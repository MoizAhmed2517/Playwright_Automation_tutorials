from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    
    select_dropdown = page.query_selector('//select[@id="Skills"]')
    select_dropdown.select_option(label='Analytics')
    
    #Much better version
    page.select_option('//select[@id="Skills"]', label="APIs")
    
    page.wait_for_timeout(2000)
    print(page.title())
    browser.close()