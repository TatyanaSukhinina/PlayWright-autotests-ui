from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.menu = CourseViewMenuComponent(page)

        self.course_view = CourseViewComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_item.nth(index)).to_be_visible()
        self.course_delete_menu_item.nth(index).click()