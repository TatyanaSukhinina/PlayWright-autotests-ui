import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
    @allure.title("Check displaying of dashboard page")
    def test_dashboard_displaying(self, dashboard_with_state_page: DashboardPage):
        dashboard_with_state_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_with_state_page.sidebar.check_visible()
        dashboard_with_state_page.dashboard.check_visible()