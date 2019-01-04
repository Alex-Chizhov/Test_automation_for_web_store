from selenium import webdriver

wd = webdriver.Chrome()
wd.implicitly_wait(20)
wd.get("http://localhost/litecart/admin/login.php")
wd.find_element_by_xpath("//input[@placeholder='Username']").send_keys("admin")
wd.find_element_by_xpath("//input[@placeholder='Password']").send_keys("admin")
wd.find_element_by_xpath("//button[@value='Login']").click()
wd.find_element_by_xpath("//i[@class='fa fa-sign-out fa-lg']").click()
wd.quit()