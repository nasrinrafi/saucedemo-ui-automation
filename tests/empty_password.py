from pages import Login_page


def test_empty_password(page):
    login=Login_page
    login.open()
    login.login("standard_user","")

    error=page.locator("[data-test='error']")
    assert error.is_visible()
