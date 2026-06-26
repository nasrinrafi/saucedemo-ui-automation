from pages.Login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_add_to_card(page):
    login=LoginPage(page)
    inventory=InventoryPage(page)
    login.login("standard_user","secret_sauce")
    inventory.add_to_cart_flee()
    des_detail=inventory.item_desc()
    inventory.click_item_desc()
    des_name=inventory.item_name()

    assert des_name==des_detail
    inventory.add_to_cart()

    assert "cart"in page.url
#def test_product_name_and_price(page):
  #  login = LoginPage(page)
   # inventory = InventoryPage(page)
    #login.login("standard_user", "secret_sauce")
   # expected_name=inventory.get_fisrd
