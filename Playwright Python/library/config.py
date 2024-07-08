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

GEM_USERNAME = os.getenv("GEMINI_USERNAME")
GEM_PASSWORD = os.getenv("GEMINI_PASSWORD")

mistral_homepage_url = "https://mistral.ai/"
mistral_chat_url = "https://chat.mistral.ai/chat"
mistral_auth_url = "https://auth.mistral.ai/ui/login/"
GPT_url = "https://chatgpt.com/"
gemini_url = "https://gemini.google.com/"
gemini_chat_url = "https://gemini.google.com/app"

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
        self.page.locator(library.locators.MEDIA_UPLOAD_BUTTON_XPATH).click()
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

class GeminiTester:
    def __init__(self, page):
        self.page = page

    def login(self):
        self.page.goto(gemini_url)
        self.page.locator(library.locators.gemini_login_cta_xpath).click()
        expect(self.page.get_by_label("Email or phone"),"Email ID field not present").to_be_visible()
        self.page.get_by_label("Email or phone").fill(GEM_USERNAME)
        self.page.get_by_text("Next").click()
        self.page.get_by_label("Enter your password").fill(GEM_PASSWORD)
        self.page.get_by_role('button', name='Next').click()
        self.page.wait_for_url(gemini_url)

    def send_message(self, message):
        self.page.locator(library.locators.gemini_message_xpath).fill(message)
        self.page.get_by_label("Send message").click()
        self.page.locator(library.locators.gemini_response_xpath).scroll_into_view_if_needed()
        self.page.wait_for_selector(library.locators.gemini_response_xpath)
        return self.page.locator(f"{library.locators.gemini_response_xpath} >> nth=0").is_visible()
    
    def send_message_2(self, message):
        expect(self.page.locator(library.locators.gemini_message_xpath)).to_be_visible()
        self.page.locator(library.locators.gemini_message_xpath).fill(message)
        expect(self.page.get_by_label("Send message")).to_be_visible()
        time.sleep(2)
        self.page.get_by_label("Send message").click()
        self.page.wait_for_selector(f"{library.locators.gemini_response_xpath} >> nth=1")
        return self.page.locator(f"{library.locators.gemini_response_xpath} >> nth=1").is_visible()

    def logout(self):
        my_profile_url = self.page.locator(library.locators.gemini_profile_cta_xpath).get_attribute('href')
        self.page.goto(my_profile_url)
        time.sleep(1)
        self.page.locator(library.locators.gemini_logout_verify_xpath).click()
        return self.page.wait_for_url(gemini_url)
    
    # def login_and_save_state(self):
        
    #     self.page.goto(gemini_url)
    #     self.page.wait_for_selector(".g-recaptcha", state="hidden")
    #     self.page.locator(library.locators.gemini_login_cta_xpath).click()
        
    #     expect(self.page.get_by_label("Email or phone"),"Email ID field not present").to_be_visible()
    #     #self.page.locator(library.locators.username_field_xpath).fill(MIS_USERNAME)
    #     self.page.get_by_label("Email or phone").fill(GEM_USERNAME)
    #     self.page.get_by_text("Next").click()
    #     # expect(self.page.get_by_test_id("node/input/password"), "Password field not present").to_be_visible()
    #     self.page.get_by_label("Enter your password").fill(GEM_PASSWORD)
    #     self.page.get_by_text("Next").click()
    #     self.page.wait_for_url("https://gemini.google.com/app")
    #     # Save storage state to a file
    #     self.page.context.storage_state(path='storage_state.json')
