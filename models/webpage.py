from playwright.async_api import Page

class Webpage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://edu.semnan.ac.ir/")
        self.the_sem_image = self.page.get_by_role("img", name="شعار سال جهش تولید")
        self.my_button = self.page.get_by_role("link", name="هيات مميزه") 
          
    def button(self):
        self.my_button.click()