from pages.Login_page import LoginPage
from tests.config import USERNAME, PASSWORD

def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/inventory.html")

    assert "inventory" in page.url