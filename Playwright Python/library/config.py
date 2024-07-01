import os
from dotenv import load_dotenv
import time
from playwright.sync_api import Playwright, sync_playwright, expect

load_dotenv()

GPT_USERNAME = os.getenv("CHATGPT_USERNAME")
GPT_PASSWORD = os.getenv("CHATGPT_PASSWORD")
GPT_url = "https://chatgpt.com/"


class ChatGPTTester:
    ASSISTANT_RESPONSE_XPATH = '//div[@data-message-author-role="assistant"]'
    MEDIA_UPLOAD_BUTTON_XPATH = '//button[@class="flex items-center justify-center text-token-text-primary juice:h-8 juice:w-8 dark:text-white juice:rounded-full focus-visible:outline-black dark:focus-visible:outline-white juice:mb-1 juice:ml-1.5"]'

    def __init__(self, page):
        self.page = page

    def login(self):
        self.page.goto(GPT_url)
        self.page.get_by_test_id("login-button").click()
        self.page.get_by_label("Email address*").fill(GPT_USERNAME)
        self.page.get_by_role("button", name="Continue", exact=True).click()
        self.page.get_by_label("Password*").fill(GPT_PASSWORD)
        self.page.click('button[type="submit"]')
        self.page.get_by_role("button", name="Continue", exact=True).click()
        self.page.wait_for_url(GPT_url)

    def logout(self):
        self.page.get_by_test_id("fruit-juice-profile").click()
        self.page.get_by_role("menuitem", name="Log out").click()
        self.page.wait_for_url(GPT_url)

    def send_message(self, message):
        self.page.get_by_placeholder("Message ChatGPT").click()
        self.page.get_by_placeholder("Message ChatGPT").fill(message)
        self.page.click('button[data-testid="fruitjuice-send-button"]')
        time.sleep(4)
        self.page.wait_for_selector(self.ASSISTANT_RESPONSE_XPATH)
        response_visible = self.page.is_visible(self.ASSISTANT_RESPONSE_XPATH)
        return response_visible
    
    def upload_file(self, file_path):
        self.page.locator(self.MEDIA_UPLOAD_BUTTON_XPATH).click()
        self.page.wait_for_timeout(4000)
        self.page.get_by_role("menuitem", name="Upload from computer").click()
        input_element_form = self.page.query_selector('input[type="file"]')
        input_element_form.set_input_files(file_path)
        time.sleep(6)
        input_element_form.close()
