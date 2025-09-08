import re

import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'create_course')

    @allure.step("Check visible courses list toolbar view")
    def check_visible(self, is_create_course_disabled=True):
        self.create_course_button.check_visible()

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

        self.title.check_visible()
        self.title.check_have_text('Courses')

    def click_create_course_button(self):
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        self.check_current_url(re.compile(".*/#/courses/create"))