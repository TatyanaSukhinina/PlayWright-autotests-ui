from components.charts.chart_view_component import ChartViewComponent
from components.dashbord.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.dashboard = DashboardToolbarViewComponent(page)

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view  = ChartViewComponent(page, "activities", "line")

    def check_all_charts_visible(self):
        self.scores_chart_view.check_visible("Scores")
        self.courses_chart_view.check_visible("Courses")
        self.students_chart_view.check_visible("Students")
        self.activities_chart_view.check_visible("Activities")



