import pytest
import os
from playwright.sync_api import sync_playwright
from library.config import ChatGPTTester

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
    assert tester.page.url == "https://chatgpt.com/"

def test_upload_image(playwright_setup):
    tester = playwright_setup
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, "Assets/test_image.jpg")
    tester.upload_file(file_path)
    tester.page.wait_for_timeout(4000)

def test_send_message(playwright_setup):
    tester = playwright_setup
    response_visible = tester.send_message("Describe this image")
    assert response_visible, "Message response not visible"

def test_logout(playwright_setup):
    tester = playwright_setup
    tester.logout()
    assert tester.page.url == "https://chatgpt.com/"
