from pages import Login_page
def test_empty_username (page):
    Login=Login_page()
    Login.open()
    Login.login("","secret_sauce")
    error=page.locator("[data-test='error']")
    assert error.is_visible()