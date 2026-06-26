from pages.cart_track import Carttracker
from pages.inventory_page import InventoryPage
def test_count_cart(logged_in_user):
    inventory=InventoryPage(logged_in_user)
    cart=Carttracker(logged_in_user)
    inventory.add_to_cart()
    before_adding_cart =cart.get_count()
    inventory.add_to_cart()
    After_adding_cart=cart.get_count()
    assert  After_adding_cart== before_adding_cart +1

