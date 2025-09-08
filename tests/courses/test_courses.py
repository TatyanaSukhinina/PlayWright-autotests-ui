import time

import allure
import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:

    @allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
    @allure.title("Check displaying of empty courses list")
    def test_test_empty_courses_list(self, courses_list_with_state_page: CoursesListPage):
        courses_list_with_state_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_with_state_page.navbar.check_visible("username")
        courses_list_with_state_page.sidebar.check_visible()

        courses_list_with_state_page.check_visible_courses_title()
        courses_list_with_state_page.check_visible_create_course_button()
        courses_list_with_state_page.check_visible_empty_view()


    @allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
    @allure.title("Edit course")
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

    @allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
    @allure.title("Create course")
    def test_create_course(self, courses_list_page: CoursesListPage,  create_course_with_state_page: CreateCoursePage):
        create_course_with_state_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_with_state_page.check_visible_create_course_title()
        create_course_with_state_page.check_disabled_create_course_button()
        create_course_with_state_page.image_upload_widget.check_visible(is_image_uploaded=False)

        create_course_with_state_page.image_upload_widget.upload_preview_image(r"C:\Users\potat\PycharmProjects\PlaywrightCourse\testdata\files\imag.png")
        create_course_with_state_page.image_upload_widget.check_visible(is_image_uploaded=True)
        time.sleep(3)

