from pages.Login_page import  LoginPage
from pages.inventory_page import InventoryPage
from  pages.cart_track import Carttracker
from pages.cart_page import cart_page
def test_verify_cart(logged_in_user):
    inventory=InventoryPage(logged_in_user)
    tracker=Carttracker(logged_in_user)
    cart=cart_page(logged_in_user)
    inventory. add_to_cart()
    init_count=tracker.get_count()
    inventory.remove_from_cart()
    new_count=cart.get_count()
    assert new_count==init_count-1

