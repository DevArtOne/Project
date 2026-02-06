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

        self.about_link = page.get_by_role("link", name= "About")
        self.downloads_link = page.get_by_role("link", name= "Downloads")
        self.documentation_link = page.get_by_role("link", name= "Documentation")
        self.community_link = page.get_by_role("link", name= "Community")
        self.StaticText = page.get_by_text("Python is a programming language that lets you work quickly")

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

    def should_have_StaticText(self):
        expect(self.StaticText).to_be_visible()