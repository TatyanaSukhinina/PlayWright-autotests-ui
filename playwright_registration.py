import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator("//input[@id = ':r0:']")
    email_input.fill("user.name@gmail.com")

    username = page.locator("//label[text() = 'Username']")
    username.fill("username")

    password_input = page.locator("//label[text() = 'Password']")
    password_input.fill("password")

    registration_btn = page.locator("#registration-page-registration-button")
    registration_btn.click()

    hider = page.get_by_test_id("dashboard-toolbar-title-text")

    expect(hider).to_be_visible()
    expect(hider).to_have_text("Dashboard")

