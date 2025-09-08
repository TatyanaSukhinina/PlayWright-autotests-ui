from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Image(page, f'{identifier}-drawer-list-item-icon', 'icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()


    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)