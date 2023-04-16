#1.Откройте https://practice.automationtesting.in/
#2. Залогиньтесь
#3. Нажмите на вкладку "Shop"
#4. Откройте книгу "HTML 5 Forms"
#5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
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
#Откройте книгу "HTML 5 Forms"
HTML=driver.find_element_by_css_selector(".post-181 h3")
HTML.click()
#Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
title = driver.title  # получение заголовка страницы
print(title)  # вывод заголовка на экран
