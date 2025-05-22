import time

import pytest
from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashbord_page import DashboardPage


@pytest.mark.regression
@pytest.mark.courses
def test_dashboard_displaying(dashboard_with_state_page: DashboardPage):
    dashboard_with_state_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_with_state_page.sidebar.check_visible()
    dashboard_with_state_page.dashboard.check_visible()

@pytest.mark.regression
@pytest.mark.courses
def test_test_empty_courses_list(courses_list_with_state_page: CoursesListPage):
    courses_list_with_state_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_with_state_page.navbar.check_visible("")
    courses_list_with_state_page.sidebar.check_visible()

    courses_list_with_state_page.check_visible_courses_title()
    courses_list_with_state_page.check_visible_create_course_button()
    courses_list_with_state_page.check_visible_empty_view()



@pytest.mark.regression
@pytest.mark.courses
def test_successful_registration(registration_page, dashboard_page):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration.fill(email='user.name@gmail.com',password='password', username='username')
    registration_page.click_registration_button()
    dashboard_page.dashboard.check_visible()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_with_state_page: CreateCoursePage):
    create_course_with_state_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_with_state_page.check_visible_create_course_title()
    create_course_with_state_page.check_disabled_create_course_button()
    create_course_with_state_page.check_visible_image_preview_empty_view()
    create_course_with_state_page.check_visible_image_upload_view()
    create_course_with_state_page.create_course_form.check_visible(
                                                        title = "",
                                                        estimated_time = "",
                                                        description = "",
                                                        max_score = "0",
                                                        min_score = "0")
    create_course_with_state_page.check_visible_exercises_title()
    create_course_with_state_page.check_visible_create_exercise_button()
    create_course_with_state_page.check_visible_exercises_empty_view()
    create_course_with_state_page.upload_preview_image(r"C:\Users\potat\PycharmProjects\PlaywrightCourse\testdata\files\imag.png")
    create_course_with_state_page.check_visible_image_upload_view()
    create_course_with_state_page.create_course_form.fill(
                                                            title = "Playwright",
                                                            estimated_time = "2 weeks",
                                                            description = "Playwright",
                                                            max_score = "100",
                                                            min_score = "10")
    create_course_with_state_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )


