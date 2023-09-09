from playwright.sync_api import Page, expect
import pytest
from creds import username, password


@pytest.fixture(autouse=True, scope="function")
def visit_web_page(page: Page):
    page.goto("https://my.semnan.ac.ir/login")

Docs_url = "https://my.semnan.ac.ir/"

def test_success(page: Page):
    username_input = page.locator("input#username")
    password_input = page.locator("input#password")
    username_input.fill(username)
    password_input.fill(password)
    button = page.locator("button#send-sms")
    button.click()

    expect(page).to_have_url(Docs_url)

def test_failure(page: Page):
    username_input = page.locator("//input[@id='username']")
    password_input = page.locator('//input[@id="password"]')
    username_input.fill("2324")
    password_input.fill("1234")
    button = page.get_by_role("button", name="ورود")
    button.click()
    dialog = page.locator('//div[@id="swal2-content"]')

    expect(dialog).to_have_text("نام کاربری و یا رمز عبور اشتباه است")