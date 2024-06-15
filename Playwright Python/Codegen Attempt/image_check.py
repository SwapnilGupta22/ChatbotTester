import os
import time
from playwright.async_api import async_playwright, expect

async def run(playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    
    await page.goto("https://chatgpt.com/")
    await page.get_by_test_id("login-button").click()
    await page.get_by_label("Email address*").click()
    await page.get_by_label("Email address*").fill("EMAIL")
    await page.get_by_role("button", name="Continue", exact=True).click()
    await page.get_by_label("Password*").click()
    await page.get_by_label("Password*").fill("PASSWORD")
    await page.get_by_role("button", name="Continue", exact=True).click()
    
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, "Assets/test_image.jpg")
    print(file_path)

    # Simulate necessary clicks to reveal the "Upload from Computer" button
    try:
        # Locate the container element and perform necessary clicks
        await page.locator(".button").click()  # Adjust the selector as needed
        await page.wait_for_timeout(2000)  # Wait for the tooltip/CTA to appear

        # Click the revealed "Upload from Computer" button
        await page.get_by_role("menuitem", name="Upload from computer").click()

        # Locate the file input element now revealed and set input files
        input_element_form = await page.query_selector('input[type="file"]')
        if input_element_form:
            await input_element_form.set_input_files(file_path)
        else:
            print("File input element in form not found.")
    except Exception as e:
        print(f"Error during file upload interaction: {e}")

    await page.wait_for_timeout(4000)
    
    await page.get_by_placeholder("Message ChatGPT").click()
    await page.get_by_placeholder("Message ChatGPT").fill("Describe this image, use the internet if needed.")
    await page.goto("https://chatgpt.com/c/e7fe57ee-86e6-46dd-8102-a8c9d82b97fb")
    await page.get_by_test_id("conversation-turn-3").locator("div").filter(has_text="ChatGPTSearched 4 sitesThe").first.click()
    await page.get_by_text("The image you uploaded").click()
    await page.get_by_text("The OnePlus 7T sports a 6.55-").click()
    await page.get_by_text("This phone runs on OxygenOS,").click()
    await page.get_by_text("Overall, the OnePlus 7T").click()
    time.sleep(10)
    await page.get_by_test_id("fruit-juice-profile").click()
    await page.get_by_role("menuitem", name="Log out").click()

    # ---------------------
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

# To run the async function
import asyncio
asyncio.run(main())
