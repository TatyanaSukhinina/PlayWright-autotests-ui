import re

from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_link = None
        self.registration_form = None
        self.registration = RegistrationFormComponent(page)

        self.registration_button = Button(page, "registration-page-registration-button", "registration_button")

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))
