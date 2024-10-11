from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")
    
    
    # css selector, id, class, attribute, tagname[attribtute==value]
    
    email_textbox = page.wait_for_selector('#email')
    email_textbox.type('test@gmail.com')
    
    loginBtn = page.wait_for_selector('#enterimg')
    loginBtn.click()
    
    page.wait_for_timeout(3000)
    browser.close()
    
#Practice same thing with another website

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # username_textbox = page.get_by_placeholder('Username')
    # OR
    username_textbox = page.wait_for_selector('input[placeholder="Username"]')
    username_textbox.type('Admin')
    
    username_textbox = page.wait_for_selector('input[placeholder="Password"]')
    username_textbox.type('admin123')
    
    btnLogin = page.wait_for_selector('button[type="submit"]')
    btnLogin.click()

    page.wait_for_timeout(3000)
    browser.close()