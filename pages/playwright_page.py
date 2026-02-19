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
        self.search_input = page.get_by_role("searchbox")
        # ----------Test main-header-------------------


        # ----------Test menubar-----------------------
        self.about_link = menubar.get_by_role("link", name="About")
        self.downloads_link = menubar.get_by_role("link", name="Downloads")
        self.documentation_link = menubar.get_by_role("link", name="Documentation")
        self.community_menubar_link = menubar.get_by_role("link", name="Community")
        # ----------Test menubar-----------------------

        # -----------Test main-content row------------------------
        # -----------Test main-content row------------------------

        # -----------Test main-content list-widgets row------------------------
        self.upcoming_events = (
            page.locator(".medium-widget.event-widget.last")
            .locator(".shrubbery")
            .locator(".menu li")
        )
        # self.first_event_text =
        self.first_event = self.upcoming_events.first
        self.all_event_text = self.upcoming_events
        # -----------Test main-content list-widgets row------------------------



        self.download_python_button = page.get_by_role("link", name="Download Python")
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
    def get_python_img(self):
        return self.python_img
        # expect(self.python_img).to_be_visible()
        # assert self.python_img.evaluate("img => img.naturalWidth > 0")
    def open_donate(self):
        self.donate_link.click()
    def search_for(self, text: str):
        self.search_input.fill(text)
        self.search_input.press("Enter")
# ----------Test main-header-------------------

# -----------Test main-content row------------------------
# -----------Test main-content row------------------------

# -----------Test main-content list-widgets row------------------------
    def get_upcoming_events(self):
        return self.upcoming_events
    def get_first_event(self):
        return self.first_event
    def check_text_events(self):
        return self.all_event_text.all_text_contents()
# -----------Test main-content list-widgets row------------------------

    # def should_have_title_python(self):
    #     expect(self.page).to_have_title(re.compile(r"Python", re.IGNORECASE))

    def click_about_link(self):
        self.about_link.click()

    def click_downloads_link(self):
        self.downloads_link.click()

    def get_download_python_button(self):
        return self.download_python_button
    def click_documentation_link(self):
        self.documentation_link.click()

    def click_community_menubar_link(self):
        self.community_menubar_link.click()

    def get_static_text(self):
        return self.static_text


    def get_support_text(self):
        return self.support_text
    def click_footer_about_link(self):
        self.footer_about_link.click()

