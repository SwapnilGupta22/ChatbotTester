import os
from dotenv import load_dotenv
import time
from playwright.sync_api import Playwright, sync_playwright, expect

load_dotenv()

USERNAME = os.getenv("MISTRAL_USERNAME")
PASSWORD = os.getenv("MISTRAL_PASSWORD")
mistral_homepage_url = "https://mistral.ai/"
mistral_chat_url = "https://chat.mistral.ai/chat"
mistral_auth_url = "https://auth.mistral.ai/ui/login/"

#locators:
login_cta_xpath = '(//a[@href="https://chat.mistral.ai/"])[3]'
username_field_xpath = 'input[name="identifier"]'
password_field_xpath = 'input[type="password"]'
submit_cta_xpath = '(//button[@type="submit"])[3]'
dialog_box_presence_xpath = '//div[@role="dialog"]'
dialog_reject_cta_xpath = '//button[@data-role="necessary"]'
chat_submit_cta_xpath = '(//button[@type="submit"])'
img_response_xpath = '(//img[@class="hidden dark:block"])[2]'
logo_count_xpath = '//img[@alt="LeChat Logo"]'

class MistralTester:

    def __init__(self, page):
        self.page = page

    def login(self):
        self.page.goto(mistral_homepage_url)
        self.page.locator(login_cta_xpath).click()
        #self.page.wait_for_url(mistral_auth_url)
        expect(self.page.get_by_test_id("node/input/identifier"),"Email ID field not present").to_be_visible()
        self.page.locator(username_field_xpath).fill(USERNAME)
        #self.page.get_by_role("button", name="Continue", exact=True).click()
        expect(self.page.get_by_test_id("node/input/password"), "Password field not present").to_be_visible()
        self.page.locator(password_field_xpath).fill(PASSWORD)
        self.page.locator(submit_cta_xpath).click()
        #self.page.get_by_role("button", name="Continue", exact=True).click()
        self.page.wait_for_url(mistral_chat_url)
        expect(self.page.locator(dialog_box_presence_xpath), "Dialog box is not present").to_be_visible()
        self.page.locator(dialog_reject_cta_xpath).click()
        expect(self.page.locator(dialog_box_presence_xpath), "Dialog Box is still visible").to_be_hidden() 

    def logout(self):
        self.page.get_by_label("User settings").click()
        self.page.get_by_text("Log out").click()
        time.sleep(4)
        expect(self.page.get_by_test_id("node/input/identifier"),"Email ID field not present").to_be_visible()

    def send_message(self, message):
        self.page.get_by_placeholder("Ask anything").fill(message)
        self.page.locator(chat_submit_cta_xpath).click()
        time.sleep(4)
        self.page.wait_for_selector(logo_count_xpath)
        #return self.page.locator(f"{logo_count_xpath} >> nth=2").is_visible()
        count = self.page.locator(logo_count_xpath).count()
        response_visible = count > 4
        return response_visible
    
    # def upload_file(self, file_path):
    #     self.page.locator(self.MEDIA_UPLOAD_BUTTON_XPATH).click()
    #     self.page.wait_for_timeout(4000)
    #     self.page.get_by_role("menuitem", name="Upload from computer").click()
    #     input_element_form = self.page.query_selector('input[type="file"]')
    #     input_element_form.set_input_files(file_path)
    #     time.sleep(6)
    #     input_element_form.close()
