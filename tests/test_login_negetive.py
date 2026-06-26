import pytest
from pages.Login_page import LoginPage

@pytest.mark.parametrize(
    "password",
    [
      "asdgh",
      "7575757",
      "%%^&&***",
    "dfgh23!@"

    ]
)
def test_negative_test(page,password):
    login=LoginPage(page)

    login.login("standard_user",password)
    error=page.locator("[data-test=error]")
    assert error.is_visible()
@pytest.mark.parametrize(
    "password,expected",
    [
        ("sdfg@1",False),

        ("shgjh@4",False),
            ("ghfdhg@#12",True),

]
  )
def test_boundray(password,expected):
    pass