from pages.dashbord.dashbord_page import DashboardPage


class TestSuite:
    def test_1(self):
        print("ddd")
        num1 = 2
        assert num1+3 == 2, "Ошибка 1"
        assert 5+5 == 11, "Ошибка 2"

    def test_2(self):
        print("sss")
        assert 5 == 5
        assert 5 < 3
        assert 5 > 3

def test_all_charts_visible(dashboard_with_state_page: DashboardPage):
    dashboard_with_state_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_with_state_page.check_all_charts_visible()
