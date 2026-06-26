from playwright.sync_api import page

class Checkout_page:
    def __init__(self, page:page):
        self.page=page

    first_name="#first-name"
    last_name="#last-name"
    postal_code="#postal-code"
    finish_button="#finish"
    complete_header=".complete-header"
    continue_button = "#continue"

    def fill_checkout(self):
        self.page.locator(self.first_name).fill("nasrin")
        self.page.locator(self.last_name).fill("rafi")
        self.page.locator(self.postal_code).fill("95014")
    def click_finsh(self):
        self.page.locator(self.finish_button).click()
    def click_continue(self):
        self.page.locator(self.continue_button).click()

    def verify_massage(self):
        return self.page.locator(self.complete_header).inner_text()

