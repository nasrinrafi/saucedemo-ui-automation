from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import cart_page

def test_validtion_price(logged_in_user):
    inventory=InventoryPage(logged_in_user)
    orginal_price=inventory.item_price()
    inventory.add_to_cart()
    inventory.item_name()
    details_price=logged_in_user.locator(".inventory_details_price").inner_text()
    assert orginal_price==details_price
    logged_in_user.go_back()
    logged_in_user.locator("shopping_cart_link").click()
    cart=cart_page(logged_in_user)
    cart_orginal_price=cart.get_product_price()
    assert cart_orginal_price==orginal_price

