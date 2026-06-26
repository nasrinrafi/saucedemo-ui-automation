class LoginPage:
    def __init__(self, page):
        self.page = page


    def open(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.wait_for_load_state("domcontentloaded")


    def login(self, user, pwd):
        self.page.locator("#user-name").wait_for(state="visible")

        self.page.locator("#user-name").fill(user)
        self.page.locator("#password").fill(pwd)
        self.page.locator("#login-button").click()