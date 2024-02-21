from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service = Service(executable_path='chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1400, 1000)
driver.get('https://sbis.ru/')
title = driver.title
print(title)
contacts_link = driver.find_element(By.LINK_TEXT, 'Контакты')
contacts_link.click()
tensor_link = driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
tensor_link.click()
print(driver.title)
elem = driver.find_element(By.XPATH, "//p[text()[contains(., 'Сила в людях')]]")
link = elem.find_element(By.LINK_TEXT, 'Подробнее')
link.click()
# check url https://tensor.ru/about
url = driver.current_url
assert url == 'https://tensor.ru/about'
# //h2[text()[contains(., 'Работаем')]]
elem = driver.find_element(By.XPATH, "//h2[text()[contains(., 'Работаем')]]/parent::div/parent::div")
images = elem.find_elements(By.TAG_NAME, 'img')
w, h = 0, 0
for img in images:
    curr_w, curr_h = img.get_attribute('width'), img.get_attribute('height')
    if not w:
        w, h = curr_w, curr_h
        continue
    assert w == curr_w
    assert h == curr_h


# img width height
driver.close()

