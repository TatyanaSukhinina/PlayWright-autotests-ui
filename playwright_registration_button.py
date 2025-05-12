import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    brawser = playwright.chromium.launch(headless=False)
    page = brawser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_btn = page.locator('#registration-page-registration-button')
    expect(registration_btn).to_be_disabled()

    email_input = page.locator("//input[@id = ':r0:']")
    email_input.fill("user.name@gmail.com")

    username_input = page.locator("//input[@id = ':r1:']")
    username_input.focus()
    username = "username"
    for letter in username:
        page.keyboard.type(letter, delay = 200)

    password_input = page.locator("//input[@id = ':r2:']")
    password_input.fill('password')

    expect(registration_btn).to_be_enabled()


