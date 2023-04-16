#1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
#2. Нажмите на вкладку "Shop"
#3. Добавьте в корзину книгу "Mastering JavaScript" (единственная книга в наличие на данный момент)
#4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹350.00"
#• Используйте для проверки assert
#5. Перейдите в корзину
#6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
#7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(15)
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
#3. Добавьте в корзину книгу "Mastering JavaScript" (единственная книга в наличие на данный момент)
Mastering_btn=driver.find_element_by_class_name("button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
Mastering_btn.click()
#4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹350.00"
#• Используйте для проверки assert

time.sleep(5)
book1=driver.find_element_by_css_selector(".cartcontents")
print(book1.text)
assert book1.text=="1 Item"
book2=driver.find_element_by_css_selector(".amount")
print(book2.text)
assert book2.text=="₹350.00"
book2.click()

#6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
#7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

Subtotal=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-subtotal")))
Total=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".order-total")))
