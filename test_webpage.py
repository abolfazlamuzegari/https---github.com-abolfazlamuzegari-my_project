from playwright.sync_api import Page, expect
from models.webpage import Webpage

def test_button(page: Page):
    homepage = Webpage(page)
    homepage.button()
    expect(homepage.page).to_have_url("https://momayeze.semnan.ac.ir/")

def test_picture(page: Page):
    homepage = Webpage(page)
    expect(homepage.the_sem_image).to_be_visible()
