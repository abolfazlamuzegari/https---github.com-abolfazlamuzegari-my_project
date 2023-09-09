from playwright.sync_api import *
import pytest

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url= "https://www.alibaba.ir"
    )
    yield api_context
    api_context.dispose()

def test_users_APi(api_context: APIRequestContext):
    Response = api_context.get("/pwa-manifest.json")

    users_data = Response.json()

    assert "name" in users_data
    assert "short_name" in users_data

    assert users_data["name"] == "علی‌بابا خرید بلیط هواپیما بلیط قطار و بلیط هواپیما خارجی"
    assert users_data["short_name"] == "علی‌بابا"

# api_context.fetch(
#     "/pwa-manifest.json/add",
#     method="POST",
#     headers={'Content-Type': 'application/json'},
#     data={
#         "firstname": "Abolfazl",
#         "lastname": "Amuzegari",
#         "age": 22
#     }
# )

# def test_create_user(api_context: APIRequestContext):
#     response = api_context.post(
#         "/pwa-manifest.json/add"
#     )
#     user_data = response.json()
    
#     assert user_data["firstname"] == "Abolfazl"