#Откройте https://practice.automationtesting.in/
#2. Нажмите на вкладку "My Account"
#3. В разделе "Login", введите email для логина
#4. В разделе "Login", введите пароль для логина
#5. Нажмите на кнопку "Login"
#6. Добавьте проверку, что на странице есть элемент "Logout"
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#2. Нажмите на вкладку "My Account"
account_btn=driver.find_element_by_css_selector ("#menu-item-50")
account_btn.click()
#3. В разделе "Login", введите email для логина
login=driver.find_element_by_css_selector("#username")
login.send_keys("89179611644@mail.ru")
#4. В разделе "Login", введите пароль для регистрации
logpwd=driver.find_element_by_css_selector("#password")
logpwd.send_keys("Lada@Lada7")
#5. Нажмите на кнопку "Login"
log_btn=driver.find_element_by_css_selector('[value="Login"]')
log_btn.click()
#6. Добавьте проверку, что на странице есть элемент "Logout"
Logout=driver.find_element_by_link_text("Logout")
print(Logout)
