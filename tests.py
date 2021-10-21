import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_buy_button(browser):
    browser.get(link)
    time.sleep(3)
    buy_btn = browser.find_element_by_xpath('//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    assert buy_btn.is_displayed(), 'Element doesn\'t displayed'
