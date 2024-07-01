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