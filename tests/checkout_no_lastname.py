from pages.checkout_page import Checkout_page
from pages.inventory_page import InventoryPage
from pages.Login_page import LoginPage
from playwright.sync_api import expect


def checkout_noName(logged_in_user):
    login=LoginPage(logged_in_user)
    inventory =InventoryPage(logged_in_user)
    inventory.add_to_cart()
    logged_in_user.locatore(".shopping_cart_link").click()

    check_out=Checkout_page(logged_in_user)
    check_out.fill_checkout("","","95014")
    expect (logged_in_user.locatore("[data-test='error']")).to_be_visible()

    #error=logged_in_user.locator("[data-test='error']")

