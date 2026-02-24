import re

from pages.playwright_page import PythonPage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, expect

# --------------------------------
""" helper‑функція, щоб стабільно перевіряти переходи, коли лінк може:
1.
Відкритися в новій вкладці (popup)
2.
Відкритися в цій же вкладці"""
def click_link_and_expect_url(page, click_fn, expected_url, popup_timeout_ms=2000):
    try:
        with page.context.expect_page(timeout=popup_timeout_ms) as popup_info:
            click_fn()
        popup_page = popup_info.value
        expect(popup_page).to_have_url(expected_url)
    except PlaywrightTimeoutError:
        expect(page).to_have_url(expected_url)
#--------------------------------


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

# ----------Test top-bar-----------------------
def test_psf_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_psf_link()
    expect(page).to_have_url("https://www.python.org/psf-landing/")
def test_docs_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    click_link_and_expect_url(
        page, home_page.click_docs_link, "https://docs.python.org/3/"
    )
def test_pypi_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    click_link_and_expect_url(page, home_page.click_pypi_link, "https://pypi.org/")
def test_jobs_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_jobs_link()
    expect(page).to_have_url("https://www.python.org/jobs/")
def test_community_top_bar_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_community_top_bar_link()
    expect(page).to_have_url("https://www.python.org/community/")
def test_python_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_python_link()
    expect(page).to_have_url("https://www.python.org/")
# ----------Test top-bar-----------------------

# ----------Test main-header-------------------
def test_python_img(page):
    home_page = PythonPage(page)
    home_page.open()
    # home_page.get_python_img()   - він необхідний, якщо expect та assert знаходяться в методах
    expect(home_page.get_python_img()).to_be_visible()
    assert home_page.get_python_img().evaluate("img => img.naturalWidth > 0")
def test_search_playwright_with_enter(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.search_for("playwright")
    expect(page).to_have_url(re.compile(r"/search/"))
# ----------Test main-header-------------------

# ----------Test menubar-----------------------
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
    expect(home_page.get_download_python_button()).to_be_visible()


def test_documentation_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_documentation_link()
    expect(page).to_have_url("https://www.python.org/doc/")

def test_community_menubar_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_community_menubar_link()
    expect(page).to_have_url("https://www.python.org/community/")
# ----------Test Downloads menu-----------------------
def test_first_releases_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open_downloads()
    home_page.click_first_releases()
    expect(page).to_have_url(re.compile(r"/release/"))
# ----------Test Downloads menu-----------------------
# ----------Test menubar-----------------------

# -----------Test main-content list-widgets row------------------------
def test_upcoming_events(page):
    home_page = PythonPage(page)
    home_page.open()
    # expect(self.upcoming_events).to_have_count(5)  інший спочіб перевірити кількість елементів
    assert home_page.get_upcoming_events().count() == 5
def test_first_event_text(page):
    home_page = PythonPage(page)
    home_page.open()
    expect(home_page.get_first_event()).to_be_visible()
    expect(home_page.get_first_event()).to_contain_text(re.compile(r"\d{4}-\d{2}-\d{2}"))
    # Це регулярний вираз. Він перевіряє, що текст починається з дати у форматі YYYY-MM-DD, далі є пробіли і будь‑який текст.Розбір: \d{4} — 4 цифри (рік),  - — дефіс,  \d{2} — 2 цифри (місяць),  - — дефіс,  \d{2} — 2 цифри (день),  \s+ — один або більше пробілів,   .+ — будь‑який текст після дати

def test_first_event_link(page):
    home_page = PythonPage(page)
    home_page.open()
    click_link_and_expect_url(
        page,
        home_page.click_first_event_link,
        re.compile(r"/events/")
    )
def test_all_events_text(page):
    home_page = PythonPage(page)
    home_page.open()
    texts = home_page.check_text_events()
    print(texts)
    assert len(texts) > 0
    assert any("PyCon" in t for t in texts)
    """Розбір:
for t in texts проходить всі рядки
"PyCon" in t перевіряє, чи є це слово всередині рядка
any(...) повертає True, якщо хоча б один рядок містить "PyCon"
Якщо жоден не містить — тест впаде."""
# -----------Test main-content list-widgets row------------------------

def test_open_python_home(page):
    home_page = PythonPage(page)
    home_page.open()
    expect(home_page.get_static_text()).to_be_visible()
    expect(page).to_have_title(re.compile(r"Python", re.IGNORECASE))
    # home_page.should_have_title_python()



def test_donate_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.open_donate()
    expect(page).to_have_url("https://www.python.org/psf/donations/")
    expect(home_page.get_support_text()).to_be_visible()


def test_footer_about_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open()
    home_page.click_footer_about_link()
    expect(page).to_have_url("https://www.python.org/about/")

# def test_should_have_img(page):
#     home_page = PythonPage(page)
#     home_page.open()
#     expect(page.python_img).to_be_visible()
#     assert page.python_img.evaluate("img => img.naturalWidth > 0")

