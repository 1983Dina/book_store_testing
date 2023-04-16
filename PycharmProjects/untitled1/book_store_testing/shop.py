#1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
#2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
#3. Добавьте в корзину книгу "Mastering JavaScript" (единственная книга в наличие на данный момент)
#4. Перейдите в корзину
#5. Нажмите "PROCEED TO CHECKOUT"
#• Перед нажатием, добавьте явное ожидание
#6. Заполните все обязательные поля
#• Перед заполнением first name, добавьте явное ожидание
#• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
#• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
#7. Выберите способ оплаты "Check Payments"
#• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
#8. Нажмите PLACE ORDER
#9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
#10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver=webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(15)
driver.maximize_window()
#Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop_tab=driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0,300);")
#3. Добавьте в корзину книгу "Mastering JavaScript" (единственная книга в наличие на данный момент)
Mastering_btn=driver.find_element_by_class_name("button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
Mastering_btn.click()
#4. Перейдите в корзину
#cart=driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0')
time.sleep(5)
cart=driver.find_element_by_css_selector('.wpmenucart-contents')
cart.click()

#5. Нажмите "PROCEED TO CHECKOUT"
check=driver.find_element_by_css_selector('.checkout-button')
check.click()

#6. Заполните все обязательные поля
#• Перед заполнением first name, добавьте явное ожидание
#• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
#• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
time.sleep(5)
first_name_field=driver.find_element_by_id("billing_first_name")
first_name_field.send_keys("Dina")
last_name_field=driver.find_element_by_id("billing_last_name")
last_name_field.send_keys("Stroganova")
email_field=driver.find_element_by_id("billing_email")
email_field.send_keys("89179611644@mail.ru")
phone_field=driver.find_element_by_id("billing_phone")
phone_field.send_keys("89179611644")
country_field_sel1=driver.find_element_by_id("s2id_billing_country")
country_field_sel1.click()
country_field_sel1=driver.find_element_by_id("s2id_autogen1_search")
country_field_sel1.send_keys("Russia")
country_field_sel2=driver.find_element_by_class_name("select2-match")
country_field_sel2.click()
address_1_field=driver.find_element_by_id("billing_address_1")
address_1_field.send_keys("ул. Автостроителей")
city_field=driver.find_element_by_id("billing_city")
city_field.send_keys("Тольятти")
state_field=driver.find_element_by_id("billing_state")
state_field.send_keys("Самарская обл.")
postcode_field=driver.find_element_by_id("billing_postcode")
postcode_field.send_keys("445039")

#7. Выберите способ оплаты "Check Payments"
#• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
driver.find_element_by_css_selector("#payment_method_cheque[value='cheque']").click()

#8. Нажмите PLACE ORDER
driver.find_element_by_css_selector("#place_order").click()

#9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
status=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
print(status)
#10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
status=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))
print(status)

