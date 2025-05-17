import pytest
from playwright.sync_api import Page
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