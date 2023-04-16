#Shop: отображение, скидка товара
#Откройте https://practice.automationtesting.in/
#Залогиньтесь
#Нажмите на вкладку "Shop"
#Откройте книгу "Android Quick Start Guide"
#Добавьте тест, что содержимое старой цены = "₹600.00" используйте assert
#Добавьте тест, что содержимое новой цены = "₹450.00" используйте assert
#Добавьте явное ожидание и нажмите на обложку книги
#Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
#Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#Залогиньтесь
my_account_menu=driver.find_element_by_link_text("My Account")
my_account_menu.click()
user_name_field=driver.find_element_by_id("username")
user_name_field.send_keys("SomeHardPassword123!@#!@#")
login_btn=driver.find_element_by_name("login")
login_btn.click()
#Нажмите на вкладку "Shop"
shop_tab=driver.find_element_by_link_text("Shop")
shop_tab.click()
#Откройте книгу "Android Quick Start Guide"
android_quick_start_book=driver.find_element_by_css_selector(".post-169 h3")
android_quick_start_book.click()
#Получение значения новой и старой цены
book_old_price=driver.find_element_by_css_selector(".price>del>span")
book_old_price_text=book_old_price.text
book_new_price=driver.find_element_by_css_selector(".price>ins>span")
book_new_price_text=book_new_price.text
#Проверка значения цен
assert book_old_price_text=="₹600.00"
assert book_new_price_text=="₹450.00"
#Добавьте явное ожидание и нажмите на обложку книги
book_cover=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()