import time

import pytest
from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Page

@pytest.mark.regression
@pytest.mark.courses
def test_successful_registration(registration_page, dashboard_page):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_email_form(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_course_with_state_page, courses_list_page):
    create_course_with_state_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_with_state_page.check_visible_create_course_title()
    create_course_with_state_page.check_disabled_create_course_button()
    create_course_with_state_page.check_visible_image_preview_empty_view()
    create_course_with_state_page.check_visible_image_upload_view()
    create_course_with_state_page.check_visible_create_course_form(
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
    create_course_with_state_page.fill_create_course_form(
                                                            title = "Playwright",
                                                            estimated_time = "2 weeks",
                                                            description = "Playwright",
                                                            max_score = "100",
                                                            min_score = "10")
    create_course_with_state_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(index = 0,
                                                title = "Playwright",
                                                estimated_time = "2 weeks",
                                                max_score = "100",
                                                min_score = "10")



@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    time.sleep(5)
    courses_hider = chromium_page_with_state.locator("//h6[text() = 'Courses']")
    expect(courses_hider).to_be_visible()

    empty_view_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_view_icon).to_be_visible()

    empty_view_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text("There is no results")

    empty_view_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")
