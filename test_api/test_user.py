import requests
import pytest
import allure

Base_URL = "https://httpbin.org"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Content-Type": "application/json"
}


@allure.feature("User Management API")
@allure.story("Get Users List")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("This test validates pagination arguments using httpbin")
@allure.link("https://httpbin.org", name="API Documentation")
def test_get_all_user_list():
    with allure.step("1. Sending GET request to server"):
        # 🛠️ اصلاح مسیر: در httpbin باید به endpoint یعنی /get بفرستیم
        response = requests.get(f"{Base_URL}/get", params={"page": 2}, headers=HEADERS)
        response_body = response.json()

    with allure.step("2. Validating response status is 200 OK"):
        assert response.status_code == 200

    with allure.step("3. Verifying pagination data"):
        # 🛠️ اصلاح بررسی دیتا: httpbin پارامترها را در کلید args و به صورت String برمی‌گرداند
        assert response_body["args"]["page"] == "2"


@allure.feature("User Management API")
@allure.story("Get User Details")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_signal_details():
    user_id = 2
    with allure.step(f"1. Sending GET request for user ID: {user_id}"):
        # 🛠️ اصلاح مسیر به /get
        response = requests.get(f"{Base_URL}/get", params={"id": user_id}, headers=HEADERS)

    with allure.step("2. Validation response status is 200 OK"):
        assert response.status_code == 200

    with allure.step("3. Verifying specific user data field"):
        user_data = response.json()
        # 🛠️ اصلاح بررسی دیتا: آیدی فرستاده شده در args ذخیره می‌شود
        assert user_data["args"]["id"] == str(user_id)


@allure.feature("User Management API")
@allure.story("Create New User")
@allure.severity(allure.severity_level.CRITICAL)
def test_creat_new_user():
    payload = {
        "name": "Ross",
        "job": "QA"
    }
    with allure.step("1. Sending POST request with new user payload"):
        # 🛠️ اصلاح مسیر: برای ارسال داده باید به /post بفرستیم
        response = requests.post(f"{Base_URL}/post", json=payload, headers=HEADERS)

    with allure.step("2. Validate specific code is 200"):
        # 🛠️ اصلاح کد وضعیت: متد post در httpbin وضعیت 200 برمی‌گرداند
        assert response.status_code == 200

    with allure.step("3. Verifying server returns correct data"):
        response_body = response.json()
        # 🛠️ اصلاح بررسی دیتا: دیتای ارسالی ما در کلید json قرار می‌گیرد
        assert response_body["json"]["name"] == payload["name"]
        assert response_body["json"]["job"] == payload["job"]


# negative test
@allure.feature("user mangmnet API")
@allure.story("negative testing")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("ensure recive 404 when endpoint dosnot exit")

def test_endpoint_not_found(api_config):
    with allure.step("1.requesting a non-exiting endpoint"):
        response = requests.get(
            f"{api_config['base_url']}/status/404",
            headers=api_config['headers']
        )

        with allure.step("2. Verifying server returns 404 Status Code"):

            assert response.status_code == 404


