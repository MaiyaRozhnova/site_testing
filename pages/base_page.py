class BasePage:
    def __init__(self, browser) -> None:
        self.browser = browser

    @property
    def url(self) -> str:
        return self.browser.current_url
