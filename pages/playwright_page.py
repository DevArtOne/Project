import re

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

        top_bar = page.get_by_role("navigation").first
        menubar = page.get_by_role("menubar")
        footer = page.get_by_role("contentinfo")

        # ----------Test top-bar-----------------------
        self.psf_link = top_bar.get_by_role("link", name="PSF")
        self.docs_link = top_bar.get_by_role("link", name="Docs")
        self.pypi_link = top_bar.get_by_role("link", name="PyPI")
        self.jobs_link = top_bar.get_by_role("link", name="Jobs")
        self.community_top_bar_link = top_bar.get_by_role("link", name="Community")
        self.python_link = top_bar.get_by_role("link", name="Python")
        # ----------Test top-bar-----------------------

        # ----------Test main-header-------------------
        self.python_img = page.get_by_role("img", name=re.compile(r"python", re.IGNORECASE))
        self.donate_link = page.get_by_role("link", name="Donate", exact=True)
        # ----------Test main-header-------------------


        # ----------Test menubar-----------------------
        self.about_link = menubar.get_by_role("link", name="About")
        self.downloads_link = menubar.get_by_role("link", name="Downloads")
        self.documentation_link = menubar.get_by_role("link", name="Documentation")
        self.community_menubar_link = menubar.get_by_role("link", name="Community")
        # ----------Test menubar-----------------------

        self.static_text = page.locator(".introduction p").filter(
            has_text=re.compile(r"Python is a programming language", re.IGNORECASE)
        ).first

        self.support_text = page.get_by_role(
            "heading",
            name=re.compile(r"Support the PSF", re.IGNORECASE),
        )
        self.footer_about_link = footer.get_by_role("link", name="About")


    def open(self):
        self.page.goto("https://www.python.org/")

# ----------Test top-bar-----------------------
    def click_psf_link(self):
        self.psf_link.click()
    def click_docs_link(self):
        self.docs_link.click()
    def click_pypi_link(self):
        self.pypi_link.click()
    def click_jobs_link(self):
        self.jobs_link.click()
    def click_community_top_bar_link(self):
        self.community_top_bar_link.click()
    def click_python_link(self):
        self.python_link.click()
# ----------Test top-bar-----------------------

# ----------Test main-header-------------------
    def should_have_img(self):
        expect(self.python_img).to_be_visible()
        assert self.python_img.evaluate("img => img.naturalWidth > 0")
# ----------Test main-header-------------------

    def click_about_link(self):
        self.about_link.click()

    def click_downloads_link(self):
        self.downloads_link.click()

    def click_documentation_link(self):
        self.documentation_link.click()

    def click_community_menubar_link(self):
        self.community_menubar_link.click()

    def should_have_static_text(self):
        expect(self.static_text).to_be_visible()

    def open_donate_and_should_have_main_header(self):
        self.donate_link.click()
        expect(self.support_text).to_be_visible()

    def click_footer_about_link(self):
        self.footer_about_link.click()

