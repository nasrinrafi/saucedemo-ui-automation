from pages.checkout_page import Checkout_page
from pages.Login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_checkout(logged_in_user):

    inventory=InventoryPage(logged_in_user)
    inventory.add_to_cart()
    expect (logged_in_user.locator(".shopping_cart_badge")).to_have_text("1")

    logged_in_user.locator(".shopping_cart_link").click()

    logged_in_user.locator("#checkout").click()

    #make object and name checkout
    checkout=Checkout_page(logged_in_user)
    checkout.fill_checkout()("nasrin","rafi","95014")

    checkout.click_continue()
    checkout.click_finsh()

    expect(LoginPage.locator(".complete-header")).to_have_text("Thank you for your order!")



