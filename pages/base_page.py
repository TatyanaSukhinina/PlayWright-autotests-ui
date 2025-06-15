from re import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        """ Данный метод открывает ссылки
            Args:
        url: URL-адрес для перехода.
        """
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """ Данный метод перезагружает страницу """
        self.page.reload(wait_until='domcontentloaded')

    # Метод для проверки текущего URL
    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)
