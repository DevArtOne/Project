from playwright.sync_api import Page, expect

# class PlaywrightHomePage:
#     def __init__(self, page: Page):
#         self.page = page
#
#         self.get_started_link = page.get_by_role("link", name= "Get started")
#         self.docs_link = page.get_by_role("link", name= "Docs")
#         self.header = page.get_by_role("heading", name= "Playwright")
#
#     def open(self):
#         self.page.goto("https://playwright.dev")
#
#     def click_get_started(self):
#         self.get_started_link.click()
#
#     def click_docs(self):
#         self.docs_link.click()
#
#     def should_have_main_header(self):
#         expect(self.header).to_be_visible()


class PythonPage:
    def __init__(self, page: Page):
        self.page = page

        menubar = page.get_by_role("menubar")

        self.about_link = menubar.get_by_role("link", name= "About", exact=True)
        self.downloads_link = menubar.get_by_role("link", name= "Downloads", exact=True)
        self.documentation_link = menubar.get_by_role("link", name= "Documentation", exact=True)
        self.community_link = menubar.get_by_role("link", name= "Community", exact=True)
        self.static_text  = page.locator(".introduction p").filter(has_text="Python is a programming language that lets you work quickly").first

    def open(self):
        self.page.goto("https://www.python.org/")

    def click_about_link(self):
        self.about_link.click()

    def click_downloads_link(self):
        self.downloads_link.click()

    def click_documentation_link(self):
        self.documentation_link.click()

    def click_community_link(self):
        self.community_link.click()

    def should_have_static_text(self):
        expect(self.static_text ).to_be_visible()
