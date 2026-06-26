class Carttracker:
    def __init__(self,page):
        self.page=page
    def get_count(self):
        cart_count=self.page.locator(".shopping_cart_badge")
        if cart_count.count()==0:
            return  0
        return int(cart_count.inner_text())



