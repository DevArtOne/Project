import re

import pytest

from pages.python_page import PythonPage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, expect

# --------------------------------
r""" helper‑функція, щоб стабільно перевіряти переходи, коли лінк може:
1.Відкритися в новій вкладці (popup)
2.Відкритися в цій же вкладці"""

#Без page.wait_for_load_state
# def click_link_and_expect_url(page, click_fn, expected_url, popup_timeout_ms=2000):
#     try:
#         with page.context.expect_page(timeout=popup_timeout_ms) as popup_info:
#             click_fn()
#         popup_page = popup_info.value
#         expect(popup_page).to_have_url(expected_url)
#     except PlaywrightTimeoutError:
#         expect(page).to_have_url(expected_url)

#З page.wait_for_load_state
def click_link_and_expect_url(page, click_fn, expected_url, popup_timeout_ms=2000, wait_state=None):
    try:
        with page.context.expect_page(timeout=popup_timeout_ms) as popup_info:
            click_fn()
        popup_page = popup_info.value
        if wait_state:
            popup_page.wait_for_load_state(wait_state)
        expect(popup_page).to_have_url(expected_url)
    except PlaywrightTimeoutError:
        if wait_state:
            page.wait_for_load_state(wait_state)
        expect(page).to_have_url(expected_url)
#--------------------------------

@pytest.fixture
def home_page(page):
    obj = PythonPage(page)
    obj.open()
    return obj


# ----------top-bar-----------------------
def test_psf_link_navigation(home_page, page):
    home_page.click_psf_link()
    expect(page).to_have_url(re.compile(r"/psf-landing/"))
def test_docs_link_navigation(home_page, page):
    click_link_and_expect_url(
        page, home_page.click_docs_link, "https://docs.python.org/3/"
    )
def test_pypi_link_navigation(home_page, page):
    click_link_and_expect_url(
        page, home_page.click_pypi_link, "https://pypi.org/"
    )
def test_jobs_link_navigation(home_page, page):
    home_page.click_jobs_link()
    expect(page).to_have_url(re.compile("/jobs/"))
def test_community_top_bar_link_navigation(home_page, page):
    home_page.click_community_top_bar_link()
    expect(page).to_have_url(re.compile("/community/"))
def test_python_link_navigation(home_page, page):
    home_page.click_python_link()
    expect(page).to_have_url("https://www.python.org/")
# ----------top-bar-----------------------

# ----------main-header-------------------
def test_python_img(home_page):
    # home_page.get_python_img()   - він необхідний, якщо expect та assert знаходяться в методах
    expect(home_page.get_python_img()).to_be_visible()
    assert home_page.get_python_img().evaluate("img => img.naturalWidth > 0")
    r"""evaluate виконує передану функцію в контексті сторінки. 
    Тут перевіряється, що в елемента img є завантажений піксельний ресурс: 
    naturalWidth > 0 означає, що зображення успішно завантажилось."""
def test_search_visible(home_page):
    expect(home_page.search_form_is_visible()).to_be_visible()
def test_search_playwright_with_enter(home_page, page):
    home_page.search_for("playwright")
    expect(page).to_have_url(re.compile(r"/search/"))
def test_button_go_click(home_page, page):
    expect(home_page.search_form_is_visible()).to_be_visible()
    home_page.click_go_button("Download")
    expect(page).to_have_url(re.compile(r"/search/\?q=Download(&.*)?$"))
    page.wait_for_load_state("domcontentloaded")
"""
(&.*)? — необов’язковий блок:
& — початок додаткових параметрів,
.* — будь-які символи (інші параметри),
? — робить весь блок опційним.
$ — кінець рядка.
"""
# ----------main-header-------------------

# ----------menubar-----------------------
def test_main_menu(home_page):
    assert home_page.get_menu_items().count() == 7
# def test_click_community_main_menu(home_page, page):
#     home_page.click_community_main_menu()
#     expect(page).to_have_url(re.compile("/community/"))

def test_about_link_navigation(home_page, page):
    home_page.click_about_link()
    expect(page).to_have_url(re.compile("/about/"))

def test_downloads_link_navigation(home_page, page):
    home_page.click_downloads_link()
    expect(page).to_have_url(re.compile("/downloads/"))
    expect(home_page.get_download_python_button()).to_be_visible()


def test_documentation_link_navigation(home_page, page):
    home_page.click_documentation_link()
    expect(page).to_have_url(re.compile("/doc/"))

def test_community_menubar_link_navigation(home_page, page):
    home_page.click_community_menubar_link()
    expect(page).to_have_url(re.compile("/community/"))
# ----------Downloads menu-----------------------

# ----------Downloads menu-----------------------
# ----------menubar-----------------------


#------------medium-widget blog-widget--------------------
def test_news_items(home_page):
    expect(home_page.get_news_items().first).to_be_visible()
    count = home_page.get_news_items().count()
    number = 3
    assert count > number, (
        f'Expected more than {number} news items, but got {count}'
    )

def test_firs_new(home_page, page):
    # expect(home_page.click_first_news()).to_be_visible()
    click_link_and_expect_url(
        page,
        home_page.click_first_news,
        re.compile(r"^https://(blog\.python\.org|pyfound\.blogspot\.com)/"),
        wait_state="domcontentloaded" #З інтеграцією в хелпер функцію
    )
    # page.wait_for_load_state("domcontentloaded")  #Без інтеграції в хелпер функцію
    r"""
    ^ — початок рядка;
    https:// — literal схема;
    \. - екранування крапки, щоб означати крапку, а не будь-який символ
    (blog\.python\.org|pyfound\.blogspot\.com) — група з двома варіантами через | (або).
    blog\.python\.org — домен blog.python.org (крапки екрановані).
    pyfound\.blogspot\.com — домен pyfound.blogspot.com (крапки екрановані).
    / — обов’язний слеш після домену
    """

def test_first_python_news(home_page, page):
    click_link_and_expect_url(
        page,
        home_page.click_first_python_new,
        re.compile(r"^https://(blog\.python\.org|pyfound\.blogspot\.com)/")
    )
#------------medium-widget blog-widget--------------------

# -----------medium-widget event-widget last------------------------
def test_upcoming_events(home_page):
    # expect(self.get_upcoming_events()).to_have_count(5)  інший спочіб перевірити кількість елементів
    assert home_page.get_upcoming_events().count() >= 1  # count() >= 1 - перевіряємо, що кількість івентів більше 0, для перевірки конкретної кількості: count() == 5
def test_first_event_text(home_page):
    expect(home_page.get_first_event()).to_be_visible()
    expect(home_page.get_first_event()).to_contain_text(re.compile(r"\d{4}-\d{2}-\d{2}"))
    r""" Це регулярний вираз. 
    Він перевіряє, що текст починається з дати у форматі YYYY-MM-DD, 
    далі є пробіли і будь‑який текст.Розбір: 
    \d{4} — 4 цифри (рік),
    - — дефіс,  
    \d{2} — 2 цифри (місяць),
    - — дефіс,  
    \d{2} — 2 цифри (день),  
    \s+ — один або більше пробілів,   
    .+ — будь‑який текст після дати
    """

def test_event_count(home_page):
    # Вимога >3 нестабільна, бо на сайті може бути менше 4 івентів.
    # Перевіряємо, що є хоча б один.
    home_page.wait_for_events_more_than(0)
def test_first_event_link(home_page, page):
    click_link_and_expect_url(
        page,
        home_page.click_first_event_link,
        re.compile(r"/events/")
    )
def test_all_events_text(home_page, page):
    texts = home_page.check_text_events()
    print(texts)
    assert len(texts) > 0
    assert any("PyCon" in t for t in texts)
    r"""Розбір:
    for t in texts проходить всі рядки
    "PyCon" in t перевіряє, чи є це слово всередині рядка
    any(...) повертає True, якщо хоча б один рядок містить "PyCon"
    Якщо жоден не містить — тест впаде."""
# -----------medium-widget event-widget last------------------------

#------------psf-widget-------------------------------------------
def test_python_img_2(home_page):
    print(expect)
    expect(home_page.get_python_img_2()).to_have_css("background", re.compile(r"python-logo-large"))
#------------psf-widget-------------------------------------------

# ------------main-footer-links-----------------------------------------
def test_first_releases_link_navigation(page):
    home_page = PythonPage(page)
    home_page.open_downloads()
    home_page.click_first_releases()
    expect(page).to_have_url(re.compile(r"/release/"))
# ------------main-footer-links-----------------------------------------

def test_open_python_home(home_page, page):
    expect(home_page.get_static_text()).to_be_visible()
    expect(page).to_have_title(re.compile(r"Python", re.IGNORECASE))
    # home_page.should_have_title_python()
    """re.IGNORECASE — цепрапорець модуля re в Python, 
    який робить пошук / порівняння регулярних виразів нечутливим до регістру.
    Наприклад, патерн abc знайде AbC, ABC, abc"""


def test_donate_link_navigation(home_page, page):
    home_page.open_donate()
    expect(page).to_have_url(re.compile("/donations/"))
    expect(home_page.get_support_text()).to_be_visible()


def test_footer_about_link_navigation(home_page, page):
    home_page.click_footer_about_link()
    expect(page).to_have_url(re.compile("/about/"))

# def test_should_have_img(page):
#     home_page = PythonPage(page)
#     home_page.open()
#     expect(page.python_img).to_be_visible()
#     assert page.python_img.evaluate("img => img.naturalWidth > 0")

