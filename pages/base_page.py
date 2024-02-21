from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    @property
    def url(self) -> str:
        return self.browser.current_url

    @property
    def title(self) -> str:
        return self.browser.title
