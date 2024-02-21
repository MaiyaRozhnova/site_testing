import time
from pages.base_page import BasePage
from pages.tensor import TensorMainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class SbisMainPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def open(self) -> None:
        self.browser.get('https://sbis.ru/')

    def contacts(self):
        element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Контакты')))
        return element

    def click_contacts(self):
        self.contacts().click()
        return SbisContactsPage(self.browser)


class SbisContactsPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def tensor_link(self):
        element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')))
        return element

    def click_tensor_link(self):
        self.tensor_link().click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return TensorMainPage(self.browser)

    def region(self):
        element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')))
        return element

    def region_name(self):
        region_elem = self.region()
        return region_elem.text

    def partners(self):
        return self.browser.find_elements(By.CLASS_NAME, "sbisru-Contacts-List__item")

    def partners_city(self):
        return self.browser.find_element(By.ID, 'city-id-2').text

    def change_region(self, new_region):
        old_title = self.title
        self.region().click()
        xpath = f"//span[text()[contains(., '{new_region}')]]"
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        self.wait.until_not(EC.title_is(old_title))
