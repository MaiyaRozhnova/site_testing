from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TensorMainPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def block_sila_v_ludyah(self):
        return self.browser.find_elements(By.XPATH, "//p[text()[contains(., 'Сила в людях')]]")

    def about_link(self):
        elem = self.browser.find_element(By.XPATH, "//p[text()[contains(., 'Сила в людях')]]/parent::div")
        return elem.find_element(By.LINK_TEXT, 'Подробнее')

    def click_about_link(self):
        link = self.about_link()
        self.browser.execute_script("arguments[0].scrollIntoView(true);", link)
        link.click()
        return TensorAboutPage(self.browser)


class TensorAboutPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def images_from_block_rabotaem(self):
        elem = self.browser.find_element(By.XPATH, "//h2[text()[contains(., 'Работаем')]]/parent::div/parent::div")
        images = elem.find_elements(By.TAG_NAME, 'img')
        return images

    def are_images_the_same_size(self) -> bool:
        images = self.images_from_block_rabotaem()
        w, h = 0, 0
        for img in images:
            curr_w, curr_h = img.value_of_css_property('width'), img.value_of_css_property('height')
            if not w:
                w, h = curr_w, curr_h
                continue
            if w != curr_w or h != curr_h:
                return False
        return True
