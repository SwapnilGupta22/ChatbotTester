import os
from dotenv import load_dotenv
import time
from playwright.sync_api import Playwright, sync_playwright, expect
import library.locators

load_dotenv()

GPT_USERNAME = os.getenv("CHATGPT_USERNAME")
GPT_PASSWORD = os.getenv("CHATGPT_PASSWORD")

MIS_USERNAME = os.getenv("MISTRAL_USERNAME")
MIS_PASSWORD = os.getenv("MISTRAL_PASSWORD")

mistral_homepage_url = "https://mistral.ai/"
mistral_chat_url = "https://chat.mistral.ai/chat"
mistral_auth_url = "https://auth.mistral.ai/ui/login/"
GPT_url = "https://chatgpt.com/"

class ChatGPTTester:
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
        self.page.wait_for_selector(library.locators.ASSISTANT_RESPONSE_XPATH)
        response_visible = self.page.is_visible(library.locators.ASSISTANT_RESPONSE_XPATH)
        return response_visible
    
    def upload_file(self, file_path):
        self.page.locator(self.MEDIA_UPLOAD_BUTTON_XPATH).click()
        self.page.wait_for_timeout(4000)
        self.page.get_by_role("menuitem", name="Upload from computer").click()
        input_element_form = self.page.query_selector('input[type="file"]')
        input_element_form.set_input_files(file_path)
        time.sleep(6)
        input_element_form.close()

class MistralTester:
    def __init__(self, page):
        self.page = page

    def login(self):
        self.page.goto(mistral_homepage_url)
        self.page.locator(library.locators.login_cta_xpath).click()
        #self.page.wait_for_url(mistral_auth_url)
        expect(self.page.get_by_test_id("node/input/identifier"),"Email ID field not present").to_be_visible()
        self.page.locator(library.locators.username_field_xpath).fill(MIS_USERNAME)
        #self.page.get_by_role("button", name="Continue", exact=True).click()
        expect(self.page.get_by_test_id("node/input/password"), "Password field not present").to_be_visible()
        self.page.locator(library.locators.password_field_xpath).fill(MIS_PASSWORD)
        self.page.locator(library.locators.submit_cta_xpath).click()
        #self.page.get_by_role("button", name="Continue", exact=True).click()
        self.page.wait_for_url(mistral_chat_url)
        expect(self.page.locator(library.locators.dialog_box_presence_xpath), "Dialog box is not present").to_be_visible()
        self.page.locator(library.locators.dialog_reject_cta_xpath).click()
        expect(self.page.locator(library.locators.dialog_box_presence_xpath), "Dialog Box is still visible").to_be_hidden() 

    def logout(self):
        self.page.get_by_label("User settings").click()
        self.page.get_by_text("Log out").click()
        time.sleep(4)
        expect(self.page.get_by_test_id("node/input/identifier"),"Email ID field not present").to_be_visible()

    def send_message(self, message):
        self.page.get_by_placeholder("Ask anything").fill(message)
        self.page.locator(library.locators.chat_submit_cta_xpath).click()
        time.sleep(4)
        self.page.wait_for_selector(library.locators.logo_count_xpath)
        #return self.page.locator(f"{logo_count_xpath} >> nth=2").is_visible()
        count = self.page.locator(library.locators.logo_count_xpath).count()
        response_visible = count > 2
        return response_visible
    
    # def upload_file(self, file_path):
    #     self.page.locator(self.MEDIA_UPLOAD_BUTTON_XPATH).click()
    #     self.page.wait_for_timeout(4000)
    #     self.page.get_by_role("menuitem", name="Upload from computer").click()
    #     input_element_form = self.page.query_selector('input[type="file"]')
    #     input_element_form.set_input_files(file_path)
    #     time.sleep(6)
    #     input_element_form.close()
