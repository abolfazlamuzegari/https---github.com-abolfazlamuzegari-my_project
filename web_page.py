from playwright.async_api import Page

class Webpage:

    def __init__(self, page: page):
        self.page = page
        self.page.goto("https://edu.semnan.ac.ir/")
        self.the_sem_image = self.page.get_by_role("img", name="شعار سال جهش تولید")
        self.drop_down_button = self.page.locator("#sm-1694178247200128-53")
        self.setup_link = self.page.get_by_text("راهنمای ثبت نام اینترنتی پذیرفته شدگان آزمون سراسری در سامانه آموزش گلستان")
    

    def button(self):
        self.drop_down_button.click()
        self.setup_link.click()