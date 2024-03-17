import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_exists(browser):
    browser.get(link)
    time.sleep(30) 
    add_to_basket_button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button') 
    assert len(add_to_basket_button) > 0, "Кнопка добавления в корзину не найдена"