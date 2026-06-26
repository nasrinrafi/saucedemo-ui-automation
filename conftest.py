import pytest
from playwright.sync_api import sync_playwright
from pages.Login_page import LoginPage
import allure

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=500)

        context = browser.new_context()

        page = context.new_page()

        yield page

        browser.close()

@pytest.fixture()
def Logged_in_user(page):
    login=LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    return page


import pytest
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()


    if rep.when == "call" and rep.failed:
        try:

            if "page" in item.funcargs:
                page = item.funcargs["page"]
                screenshot = page.screenshot(full_page=True)
                allure.attach(
                    screenshot,
                    name="Screenshot_On_Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            # اگر از Selenium استفاده میکنی و اسم فیستچرت driver هست
            elif "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Screenshot_On_Failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Error capturing screenshot: {e}")