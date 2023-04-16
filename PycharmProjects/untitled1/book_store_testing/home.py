from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0,600);")
#Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
READ_btn=driver.find_element_by_css_selector('[data-product_id="160"]')
READ_btn.click()
#4. Нажмите на вкладку "REVIEWS"
reviws_btn=driver.find_element_by_css_selector(".reviews_tab")
reviws_btn.click()

#5. Поставьте 5 звёзд
star5_btn=driver.find_element_by_css_selector(".star-5")
star5_btn.click()

#6. Заполните поле "Review" сообщением: "Nice book!"
comment=driver.find_element_by_css_selector("#comment")
comment.send_keys("Nice book!")

#7. Заполните поле "Name"
name=driver.find_element_by_css_selector("#author")
name.send_keys("Dina")

#8. Заполните "Email"
name=driver.find_element_by_css_selector("#email")
name.send_keys("Dina777@mail.ru")

#9. Нажмите на кнопку "SUBMIT"
submit_btn=driver.find_element_by_css_selector("#submit")
submit_btn.click()
