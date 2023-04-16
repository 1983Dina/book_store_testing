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
#Откройте категорию "HTML"
HTML=driver.find_element_by_css_selector(".cat-item.cat-item-19 a")
HTML.click()
#Добавьте тест, что отображается три товара
count=driver.find_element_by_css_selector(".cat-item-19 .count")
print(count.text)
