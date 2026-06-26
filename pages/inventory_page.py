import cart as cart
import page as page


class InventoryPage:
    def __init__(self, page):
        self.page = page

    # locator

    item_desc = "#inventory-item-description "
    add_to_cart = "add-to-cart"
    inventory_item_dec = "inventory-item-desc"
    inventory_item_price = "inventory-item-price"
    shopping_cart_link = "shopping-cart-link"
    continue_shopping = "continue-shopping"
    add_to_cart_flee = "add-to-cart-sauce-labs-flee"
    item_name=".inventory_item_name"
    remove_cart="remove-sauce-labs-backpack"


def item_desc(self):
   return self.page.locator(self.item_desc).first.inner_text()

def item_name(self):
    return self.page.locator(self.item_name).first.click()



def item_price(self):
    return self.page.locator(self.inventory_item_price).first.inner_text()


def add_to_cart_flee(self):
   self.page.locator(self.add_to_cart_flee).click()


def add_to_cart(self):
   self.page.locator(self.add_to_cart).click()


def continue_shopping(self):
    self.page.locator(self.continue_shopping).click()

def remove_from_cart(self):
    self.page.locator(self.remove_cart).click()


def add_backpack_to_cart(self):
  self.page.locator(self.add_backpack_btn).click()


# def open_cart(self):
#     self.page.locator(self.cart_icon).click()


# def sort_products(self, value):
#    self.page.locator(self.sort_dropdown).select_option(value)
def item_price_sort(self):
    prices=self.page.locator(".inventory_item_price").all_inner_text()
    return [float (p.replace("$","")) for p in prices]
