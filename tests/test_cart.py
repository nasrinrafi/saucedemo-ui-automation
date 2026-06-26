from playwright.sync_api import expect
def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    page.wait_for_timeout(3000)
    print(page.url)
    page.wait_for_url("**/cart.html")
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator(".shopping_cart_link").click()
    page.wait_for_url("**/cart.html")

    expect(page).to_have_url("**/cart.html")