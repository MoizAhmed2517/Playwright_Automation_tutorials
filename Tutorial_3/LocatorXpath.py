from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # using attribute - '//tagname[@attributename="value"]
    # usrName = page.wait_for_selector('//input[@name="username"]')
    # passWrd = page.wait_for_selector('//input[@placeholder="Password"]')
    # usrName.type('Admin')
    # passWrd.type('admin123')
    # login = page.wait_for_selector('//button[@type="submit"]')
    # login.click()
    # page.wait_for_timeout(3000)
    # browser.close()
    
    # using text - '//tagname[text()="text"]
    # usrName = page.wait_for_selector('//input[@name="username"]')
    # passWrd = page.wait_for_selector('//input[@placeholder="Password"]')
    # usrName.type('Admin')
    # passWrd.type('admin123')
    # login = page.wait_for_selector('//button[text()=" Login "]') #using text() you need to type as it is text written for Heading
    # login.click()
    # page.wait_for_timeout(3000)
    # browser.close()
    
    # using attributes with contain - //tagname[contains(@attribute, "Value")]
    # using text with contain - //tagname[contains(text(), "text")]
    
    usrName = page.wait_for_selector('//label[contains(text(), "Username")]')
    passWrd = page.wait_for_selector('//label[contains(text(), "Password")]')
    usrName.type('Admin')
    passWrd.type('admin123')
    login = page.wait_for_selector('//button[text()=" Login "]') #using text() you need to type as it is text written for Heading
    login.click()
    page.wait_for_timeout(3000)
    browser.close()
    
    # dynamic Username, username123, username2321
    # start-with - //tagname[starts-with(@id, 'username')]
    # ends-with - username23124
    
    # family
    # parent - //tagname[@id = "xy"]/parent::input[]
    # child - //tagname[@id = "xy"]/child::input[]
    # ancestor - 
    # siblings - //td[text()="Microsoft"]//following-sibling:: td[2] 