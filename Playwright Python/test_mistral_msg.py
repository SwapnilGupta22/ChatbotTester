import pytest
from playwright.sync_api import sync_playwright
import library.mistral
from library.mistral import MistralTester

chat_url = library.mistral.mistral_chat_url
auth_url = library.mistral.mistral_auth_url

@pytest.fixture(scope="module")
def mistral_setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        tester = MistralTester(page)
        yield tester
        context.close()
        browser.close()

def test_login(mistral_setup):
    tester = mistral_setup
    tester.login()
    assert tester.page.url == chat_url

def test_send_first_message(mistral_setup):
    tester = mistral_setup
    response_visible = tester.send_message("How are you today?")
    assert response_visible, "Second message response not visible"

def test_send_second_message(mistral_setup):
    tester = mistral_setup
    response_visible = tester.send_message("How are you today?")
    assert response_visible, "Second message response not visible"

def test_logout(mistral_setup):
    tester = mistral_setup
    tester.logout()
    #assert tester.page.url == auth_url
