from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    # page.wait_for_selector('//div[@id="OKTab"]/button')
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(2000)
    # controlling the alert function
    page.on("dialog", lambda dialog: dialog.accept())
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(2000)
    browser.close()