import time

import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashbord.dashbord_page import DashboardPage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:

    def test_dashboard_displaying(self, dashboard_with_state_page: DashboardPage):
        dashboard_with_state_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_with_state_page.sidebar.check_visible()
        dashboard_with_state_page.dashboard.check_visible()

    def test_test_empty_courses_list(self, courses_list_with_state_page: CoursesListPage):
        courses_list_with_state_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_with_state_page.navbar.check_visible("username")
        courses_list_with_state_page.sidebar.check_visible()

        courses_list_with_state_page.check_visible_courses_title()
        courses_list_with_state_page.check_visible_create_course_button()
        courses_list_with_state_page.check_visible_empty_view()

    def test_successful_registration(self, registration_page, dashboard_page):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration.fill(email='user.name@gmail.com',password='password', username='username')
        registration_page.click_registration_button()
        dashboard_page.dashboard.check_visible()

    def test_edit_course(self, create_course_with_state_page, courses_list_page):
        create_course_with_state_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_with_state_page.image_upload_widget.upload_preview_image(r"C:\Users\potat\PycharmProjects\PlaywrightCourse\testdata\files\imag.png")
        create_course_with_state_page.fill_create_course_form("Cats_math_course",
                                                              "2",
                                                              "Special maths for cats",
                                                              '200',
                                                              '20'
                                                              )

        create_course_with_state_page.click_create_exercise_button()
        create_course_with_state_page.click_create_course_button()

        courses_list_page.course_view.check_visible(0, "Cats_math_course",
                                                              '200',
                                                              '20',"2")

        courses_list_page.menu.click_edit(0)
        create_course_with_state_page.fill_create_course_form("Dogs_math_course",
                                                              "3",
                                                              "Special maths for DOGS",
                                                              '300',
                                                              '30'
                                                              )
        create_course_with_state_page.click_create_course_button()

        courses_list_page.course_view.check_visible(0, "Dogs_math_course",
                                                              '300',
                                                              '30',"3")


    def test_create_course(self, courses_list_page: CoursesListPage,  create_course_with_state_page: CreateCoursePage):
        create_course_with_state_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_with_state_page.check_visible_create_course_title()
        create_course_with_state_page.check_disabled_create_course_button()
        create_course_with_state_page.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_with_state_page.image_upload_widget.upload_preview_image(r"C:\Users\potat\PycharmProjects\PlaywrightCourse\testdata\files\imag.png")
        create_course_with_state_page.image_upload_widget.check_visible(is_image_uploaded=True)
        time.sleep(3)

    @pytest.mark.xfail
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")