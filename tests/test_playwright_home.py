from pages.playwright_page import PythonPage
from playwright.sync_api import expect

# def test_open_playwright_home(page):
#     home_page = PlaywrightHomePage(page)
#
#     home_page.open()
#     home_page.should_have_main_header()
#
# def test_get_started_navigation(page):
#     home_page = PlaywrightHomePage(page)
#
#     home_page.open()
#     home_page.click_get_started()
#
#     expect(page).to_have_url("https://playwright.dev/docs/intro")
#
# def test_docs_navigation(page):
#     home_page = PlaywrightHomePage(page)
#
#     home_page.open()
#     home_page.click_docs()
#
#     expect(page).to_have_url("https://playwright.dev/docs/intro")

def test_open_python_home(page):
    home_page = PythonPage(page)

    home_page.open()
    home_page.should_have_StaticText()

def test_about_link_navigation(page):
    home_page = PythonPage(page)

    home_page.open()
    home_page.click_about_link()

    expect(page).to_have_url("https://www.python.org/about/")

def test_downloads_link_navigation(page):
    home_page = PythonPage(page)

    home_page.open()
    home_page.click_downloads_link()

    expect(page).to_have_url("https://www.python.org/downloads/")

def test_documentation_link_navigation(page):
    home_page = PythonPage(page)

    home_page.open()
    home_page.click_documentation_link()

    expect(page).to_have_url("https://www.python.org/doc/")

def test_community_link_navigation(page):
    home_page = PythonPage(page)

    home_page.open()
    home_page.click_community_link()

    expect(page).to_have_url("https://www.python.org/community/")
