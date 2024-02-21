from pages.sbis import SbisMainPage


def test_first(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_contacts_page = sbis_page.click_contacts()
    tensor_main_page = sbis_contacts_page.click_tensor_link()
    sila_block = tensor_main_page.block_sila_v_ludyah()

    assert len(sila_block) == 1
    tensor_about_page = tensor_main_page.click_about_link()
    assert tensor_about_page.url == 'https://tensor.ru/about'
    assert tensor_about_page.are_images_the_same_size()


def test_second(browser):
    assert 2 == 2
