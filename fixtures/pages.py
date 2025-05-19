import pytest
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.registration_page import RegistrationPage
from pages.dashbord_page import DashboardPage

#В этом файле хранятся  фикстуры,
# отвечающие за инициализацию страниц.

@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)

@pytest.fixture
def create_course_page(chromium_page: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page)

@pytest.fixture
def create_course_with_state_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)

@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)