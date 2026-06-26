from playwright.sync_api import page
class cart_page:
    def __init__(self,page):
        self.page=page

    car_item=".cart_item"
    checkout_button="#checkout"
    continue_shopping_button="#continue-shopping"

    def click_checkout(self):
        self.page.locator(self.checkout_button).click()

    def continue_shopping(self):
        self.page.locator(self.continue_shopping_button).click()

    def get_cart_item_count(self):
        return self.page.locator(self.car_item).count()

    def get_product_name(self):
        return self.page.locator(".inventory_item_name").first.inner_text()

    def get_product_price(self):
        return self.page.locator(".inventory_item_price").first.inner_text()