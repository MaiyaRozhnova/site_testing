from pages.base_page import BasePage
from pages.tensor import TensorMainPage
from selenium.webdriver.common.by import By


class SbisMainPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def open(self) -> None:
        self.browser.get('https://sbis.ru/')

    def contacts(self):
        return self.browser.find_element(By.LINK_TEXT, 'Контакты')

    def click_contacts(self):
        self.contacts().click()
        return SbisContactsPage(self.browser)


class SbisContactsPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def tensor_link(self):
        return self.browser.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')

    def click_tensor_link(self):
        self.tensor_link().click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return TensorMainPage(self.browser)
