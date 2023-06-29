import re

from playwright.sync_api import Playwright, sync_playwright

# Define your login credentials
username = 'YourUsername'
password = 'YourPassowrd'

# Define the post details
title = 'My New Post'
content = 'This is the content of my new post.'
image_path = 'codesign-logo-650px.png'


# Define the Playwright script
def run(playwright: Playwright) -> None:
    # Launch a new browser instance
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context
    context = browser.new_context()

    # Create a new page object
    page = context.new_page()

    # Navigate to the WordPress login page
    page.goto('https://url/wp-admin')

    # Wait for the login page to load
    page.wait_for_selector('#user_login')

    # Fill in the login form and submit it
    page.fill('#user_login', username)
    page.fill('#user_pass', password)
    page.click('#wp-submit')

    # Wait for the WordPress dashboard to load
    page.wait_for_selector('#wp-admin-bar-site-name')

    # Navigate to the Posts page
    page.click('text=Posts')

    # Wait for the Posts page to load
    page.wait_for_selector('#wpbody-content')

    # Click the "Add New" button to create a new post
    page.click('text=Add New')

    # Fill in the post title and content
    page.get_by_role("textbox", name="Add title").click()
    page.get_by_role("textbox", name="Add title").fill(title)
    page.get_by_role("button", name="Add default block").click()
    page.get_by_role("document", name="Empty block; start writing or type forward slash to choose a block").fill(
        content)
    page.get_by_role("region", name="Editor settings").get_by_role("button", name="Post").click()
    page.wait_for_selector('#editor > div > div.edit-post-layout.is-mode-visual.is-sidebar-opened.has-metaboxes.interface-interface-skeleton.has-footer > div.interface-interface-skeleton__editor > div.interface-interface-skeleton__body > div.interface-navigable-region.interface-interface-skeleton__sidebar > div > div.components-panel > div:nth-child(4) > div')

    # Upload the featured image
    page.get_by_role("button", name="Set featured image").click()
    page.wait_for_selector('#menu-item-upload')
    page.get_by_role("searchbox", name="Search").click()
    page.get_by_role("searchbox", name="Search").fill("event")
    page.get_by_role("checkbox", name="june29-events").click()
    page.locator("div").filter(has_text=re.compile(r"^Set featured image$")).nth(4).click()
    page.get_by_role("button", name="Publish", exact=True).click()
    page.get_by_role("region", name="Editor publish").get_by_role("button", name="Publish", exact=True).click()

    # Wait for the post to be published and navigate to the post page
    page.wait_for_selector('text=View post')
    page.click('text=View post')


    # Close the browser context
    context.close()
    browser.close()
    print("posted the new article")


# Run the Playwright script
with sync_playwright() as playwright:
    run(playwright)
