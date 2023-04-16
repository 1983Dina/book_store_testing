#Откройте https://practice.automationtesting.in/
#2. Нажмите на вкладку "My Account"
#3. В разделе "Register", введите email для регистрации
#4. В разделе "Register", введите пароль для регистрации
#• составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
#• почту и пароль сохраните, потребуюутся в дальнейшем
#5. Нажмите на кнопку "Register"
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#2. Нажмите на вкладку "My Account"
account_btn=driver.find_element_by_css_selector ("#menu-item-50")
account_btn.click()
#3. В разделе "Register", введите email для регистрации
email=driver.find_element_by_css_selector("#reg_email")
email.send_keys("89179611644@mail.ru")
#4. В разделе "Register", введите пароль для регистрации
pwd=driver.find_element_by_css_selector("#reg_password")
pwd.send_keys("Lada@Lada7")
#5. Нажмите на кнопку "Register"
reg_btn=driver.find_element_by_css_selector('[value="Register"]')
reg_btn.click()
