def test_login_to_admin_panel(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.find_element_by_xpath("//input[@placeholder='Username']").send_keys("admin")
    wd.find_element_by_xpath("//input[@placeholder='Password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@value='Login']").click()
    menu_elements = wd.find_elements_by_xpath("//span[@class='name']")

    assert len(menu_elements) == 17

    wd.find_element_by_xpath("//i[@class='fa fa-sign-out fa-lg']").click()