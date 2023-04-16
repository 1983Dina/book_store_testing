from selenium import webdriver
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
#Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
#Используйте проверку по value
menu=driver.find_element_by_css_selector('[value="menu_order"]')
menu.click()
#Отсортируйте товары по цене от большей к меньшей
#в селекторах используйте класс Select
price=driver.find_element_by_css_selector ('[value="price-desc"]')
price.click()
#Снова объявите переменную с локатором основного селектора сортировки т.к после сортировки страница обновится
menu=driver.find_element_by_css_selector('[value="menu_order"]')
#Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
#Используйте проверку по value
price=driver.find_element_by_css_selector ('.orderby [selected="selected"]')
print(price.text)
