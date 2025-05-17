from playwright.sync_api import Page

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

