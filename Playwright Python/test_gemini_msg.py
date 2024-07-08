import pytest
import os
from playwright.sync_api import sync_playwright
import library.config
from library.config import GeminiTester

gemini_url = library.config.gemini_url
gemini_chat_url = library.config.gemini_chat_url

@pytest.fixture(scope="module")
def gemini_setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        tester = GeminiTester(page)
        yield tester
        context.close()
        browser.close()

def test_login(gemini_setup):
    tester = gemini_setup
    tester.login()
    assert tester.page.url == gemini_chat_url

def test_send_first_message(gemini_setup):
    tester = gemini_setup
    response_visible = tester.send_message("What is AI?")
    assert response_visible, "First message response not visible"

def test_send_second_message(gemini_setup):
    tester = gemini_setup
    response_visible = tester.send_message_2("How are you today?")
    assert response_visible, "Second message response not visible"

def test_logout(gemini_setup):
    tester = gemini_setup
    tester.logout()
    assert tester.page.url == gemini_url
