from pages.sbis import SbisMainPage


def test_tensor_images(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_contacts_page = sbis_page.click_contacts()
    tensor_main_page = sbis_contacts_page.click_tensor_link()
    sila_block = tensor_main_page.block_sila_v_ludyah()

    assert len(sila_block) == 1
    tensor_about_page = tensor_main_page.click_about_link()
    assert tensor_about_page.url == 'https://tensor.ru/about'
    assert tensor_about_page.are_images_the_same_size()


def test_regions(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_contacts_page = sbis_page.click_contacts()
    test_region = 'Нижегородская обл.'
    assert sbis_contacts_page.region_name() == test_region
    assert sbis_contacts_page.partners_city() == 'Нижний Новгород'
    test_region = 'Камчатский край'
    sbis_contacts_page.change_region(test_region)
    assert test_region in sbis_contacts_page.title
    assert 'kamchatskij-kraj' in sbis_contacts_page.url
    assert sbis_contacts_page.region_name() == test_region
    assert sbis_contacts_page.partners_city() == 'Петропавловск-Камчатский'
