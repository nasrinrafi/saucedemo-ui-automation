from pages.Login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_price(logged_in_user):
    login=LoginPage(logged_in_user)
    inventory=InventoryPage(logged_in_user)
    price=inventory.item_price_sort()
    assert price[0]==min(price)



