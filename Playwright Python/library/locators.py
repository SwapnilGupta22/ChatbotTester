#Chat GPT Locators
ASSISTANT_RESPONSE_XPATH = '//div[@data-message-author-role="assistant"]'
MEDIA_UPLOAD_BUTTON_XPATH = '//button[@class="flex items-center justify-center text-token-text-primary juice:h-8 juice:w-8 dark:text-white juice:rounded-full focus-visible:outline-black dark:focus-visible:outline-white juice:mb-1 juice:ml-1.5"]'


#Mistral AI Locators
login_cta_xpath = '(//a[@href="https://chat.mistral.ai/"])[3]'
username_field_xpath = 'input[name="identifier"]'
password_field_xpath = 'input[type="password"]'
submit_cta_xpath = '(//button[@type="submit"])[3]'
dialog_box_presence_xpath = '//div[@role="dialog"]'
dialog_reject_cta_xpath = '//button[@data-role="necessary"]'
chat_submit_cta_xpath = '(//button[@type="submit"])'
img_response_xpath = '(//img[@class="hidden dark:block"])[2]'
logo_count_xpath = '//img[@alt="LeChat Logo"]'

#Gemini AI locators
gemini_login_cta_xpath = '//button[@data-test-id="action-button"]'
gemini_message_xpath = '//div[@role="textbox"]'
gemini_response_xpath = '//*[contains(@class, "response-container-footer")]'
gemini_profile_cta_xpath = '(//a[@role="button"])[2]'
gemini_logout_cta_xpath = '//span[@class="JWEMkf"]/span[2]'
#'(//span[@jsaction="click:vyP2Ce"])[3]'
#(//a[@rel="noopener noreferrer"]/span[2]/div)[2]
