import pytest
from playwright.sync_api import sync_playwright
import library.config
from library.config import ChatGPTTester

chatgpt_url = library.config.GPT_url
@pytest.fixture(scope="module")
def playwright_setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        tester = ChatGPTTester(page)
        yield tester
        context.close()
        browser.close()

def test_login(playwright_setup):
    tester = playwright_setup
    tester.login()
    assert tester.page.url == chatgpt_url

def test_send_first_message(playwright_setup):
    tester = playwright_setup
    response_visible = tester.send_message("Hello, ChatGPT!")
    assert response_visible, "First message response not visible"

def test_send_second_message(playwright_setup):
    tester = playwright_setup
    response_visible = tester.send_message("How are you today?")
    assert response_visible, "Second message response not visible"

def test_logout(playwright_setup):
    tester = playwright_setup
    tester.logout()
    assert tester.page.url == chatgpt_url
