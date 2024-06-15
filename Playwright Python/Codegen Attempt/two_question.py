import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chatgpt.com/")
    page.get_by_test_id("login-button").click()
    page.get_by_label("Email address*").click()
    page.get_by_label("Email address*").fill("EMAIL")
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_label("Password*").fill("PASSWORD")
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_placeholder("Message ChatGPT").click()
    page.get_by_placeholder("Message ChatGPT").fill("what is 1+1 equal to?")
    page.goto("https://chatgpt.com/c/f118ebb5-2503-4da6-bfc1-19bb5bbfcd91")
    page.get_by_test_id("conversation-turn-3").locator("div").filter(has_text="ChatGPT1 + 1 equals 2.4o").first.click()
    page.get_by_text("+ 1 equals 2.").click()
    page.get_by_placeholder("Message ChatGPT").click()
    page.get_by_placeholder("Message ChatGPT").click()
    page.get_by_placeholder("Message ChatGPT").fill("thanks for the response,\nhow do I learn maths? summarize in 1 paragraph")
    page.get_by_test_id("fruitjuice-send-button").click()
    page.get_by_test_id("conversation-turn-5").locator("div").filter(has_text="ChatGPTTo learn math").first.click()
    page.get_by_text("To learn math effectively,").click()
    page.get_by_test_id("fruit-juice-profile").click()
    page.get_by_role("menuitem", name="Log out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
