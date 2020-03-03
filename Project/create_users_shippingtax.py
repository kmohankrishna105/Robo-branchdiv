from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")

#driver.get("https://dev40-na-gapinc.demandware.net/on/demandware.store/Sites-Intermix-Site/en_US/Home-Show")

driver.get("https://dev12-na-gapinc.demandware.net/on/demandware.store/Sites-Intermix-Site/en_US/Home-Show")

modalLoginRegister ="login-register"
mobLoginRegister = ".account-login-page"
tabRegister = "[data-id*='register']"
driver.implicitly_wait(10)

input("click ok on alert message")
try:
    alert1=driver.switch_to.alert
    print(alert1.text)
    alert1.find_element_by_link_text("Click here.")
except:
    print("No laert message")


import xlrd

loc = ("C:\\Users\\mkottak\\Downloads\\FireShot\\newusers_tax.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range (14,16):
    # For row 0 and column 0
    email=sheet.cell_value(i, 0)
    firname=sheet.cell_value(i, 1)
    lasname=sheet.cell_value(i, 2)
    address1=sheet.cell_value(i, 3)
    city_val = sheet.cell_value(i, 4)
    code_val= sheet.cell_value(i, 5)


    address2 = sheet.cell_value(i, 6)
    city_val2 = sheet.cell_value(i, 7)
    code_val2 = sheet.cell_value(i, 8)

    address3 = sheet.cell_value(i, 9)
    city_val3 = sheet.cell_value(i, 10)
    code_val3 = sheet.cell_value(i, 11)

    address4 = sheet.cell_value(i, 12)
    city_val4 = sheet.cell_value(i, 13)
    code_val4 = sheet.cell_value(i, 14)
    print(email)

    driver.implicitly_wait(9)
    driver.find_element_by_xpath("//a[@title='User: My Account']").click()
    #for dev12
    #driver.find_element_by_xpath("(//span)[12]").click()
    driver.implicitly_wait(10)




    try:
        driver.find_element_by_xpath("//div[contains(@data-id,'register')]").click()
        driver.find_element_by_id("dwfrm_profile_customer_firstname").send_keys(firname)
        driver.find_element_by_id("dwfrm_profile_customer_lastname").send_keys(lasname)
        driver.find_element_by_id("dwfrm_profile_customer_email").send_keys(email)
        driver.find_element_by_xpath("//input[contains(@id,'dwfrm_profile_login_password')]").send_keys("Test@123")
        driver.find_element_by_xpath("//*[contains(@id,'dwfrm_profile_login_passwordconfirm')]").send_keys("Test@123")
        driver.find_element_by_name("dwfrm_profile_confirm").click()
    except:
        print("hi")

    driver.implicitly_wait(10)
    #input("for address:")
    driver.find_element_by_xpath("(//h2[@class='account-sub-headers'][contains(text(),'Address Book')])").click()
    driver.find_element_by_xpath("//a[@class='btn-secondary']").click()
    driver.implicitly_wait(5)

    idname='dwfrm_profile_address_addressid'
    fname='dwfrm_profile_address_firstname'
    lname='dwfrm_profile_address_lastname'
    add1='dwfrm_profile_address_address1'
    city='dwfrm_profile_address_city'
    code='dwfrm_profile_address_postal'
    phone='dwfrm_profile_address_phone'
    driver.find_element_by_id(idname).send_keys("review tax")
    driver.find_element_by_id(fname).send_keys("Rula")
    driver.find_element_by_id(lname).send_keys("Elali")
    driver.find_element_by_id(add1).send_keys(address1)

    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_id('dwfrm_profile_address_country'))
    select.select_by_visible_text('United States')



    driver.find_element_by_id(city).send_keys(city_val)

    select1 = Select(driver.find_element_by_id('dwfrm_profile_address_states_state'))
    select1.select_by_visible_text('New York')

    driver.find_element_by_id(code).send_keys("10016")
    driver.find_element_by_id(phone).send_keys("800-871-0711")

    driver.find_element_by_name("dwfrm_profile_address_create").click()

    driver.implicitly_wait(10)

    """ Second address"""
    driver.find_element_by_xpath("//a[@class='btn-secondary']").click()
    driver.implicitly_wait(5)

    driver.find_element_by_id(idname).send_keys("no review tax")
    driver.find_element_by_id(fname).send_keys("David")
    driver.find_element_by_id(lname).send_keys("Surname")
    driver.find_element_by_id(add1).send_keys(address2)

    from selenium.webdriver.support.ui import Select

    select = Select(driver.find_element_by_id('dwfrm_profile_address_country'))
    select.select_by_visible_text('United States')

    driver.find_element_by_id(city).send_keys(city_val2)

    select1 = Select(driver.find_element_by_id('dwfrm_profile_address_states_state'))
    select1.select_by_visible_text('New York')

    driver.find_element_by_id(code).send_keys("10016")
    driver.find_element_by_id(phone).send_keys("800-871-0711")

    driver.find_element_by_name("dwfrm_profile_address_create").click()

    driver.implicitly_wait(10)


    """third address"""

    driver.find_element_by_xpath("//a[@class='btn-secondary']").click()
    driver.implicitly_wait(5)

    driver.find_element_by_id(idname).send_keys("review no tax")
    driver.find_element_by_id(fname).send_keys("Rula")
    driver.find_element_by_id(lname).send_keys("Elali")
    driver.find_element_by_id(add1).send_keys(address3)

    from selenium.webdriver.support.ui import Select

    select = Select(driver.find_element_by_id('dwfrm_profile_address_country'))
    select.select_by_visible_text('United States')

    driver.find_element_by_id(city).send_keys(city_val3)

    select1 = Select(driver.find_element_by_id('dwfrm_profile_address_states_state'))
    select1.select_by_visible_text('Delaware')

    driver.find_element_by_id(code).send_keys("19960")
    driver.find_element_by_id(phone).send_keys("800-871-0711")

    driver.find_element_by_name("dwfrm_profile_address_create").click()

    driver.implicitly_wait(10)

    """ fourth address"""
    driver.find_element_by_xpath("//a[@class='btn-secondary']").click()
    driver.implicitly_wait(5)

    driver.find_element_by_id(idname).send_keys("no review no tax")
    driver.find_element_by_id(fname).send_keys("David")
    driver.find_element_by_id(lname).send_keys("Surname")
    driver.find_element_by_id(add1).send_keys(address4)

    from selenium.webdriver.support.ui import Select

    select = Select(driver.find_element_by_id('dwfrm_profile_address_country'))
    select.select_by_visible_text('United States')

    driver.find_element_by_id(city).send_keys(city_val4)

    select1 = Select(driver.find_element_by_id('dwfrm_profile_address_states_state'))
    select1.select_by_visible_text('Delaware')

    driver.find_element_by_id(code).send_keys("19960")
    driver.find_element_by_id(phone).send_keys("800-871-0711")

    driver.find_element_by_name("dwfrm_profile_address_create").click()

    driver.implicitly_wait(10)

    from selenium.webdriver.common.action_chains import ActionChains
    action = ActionChains(driver)
    #wrapper > div.sticky-wrapper > div > div.top-banner > div.search-utility-nav-bag > ul > li > a


    firstLevelMenu = driver.find_element_by_css_selector("a.user-account.btn-small-flat") #id of menu, or xpath of menu, whatever
    action.move_to_element(firstLevelMenu).perform()

    secondLevelMenu = driver.find_element_by_xpath("//a[contains(@href,'/en_US/Login-Logout')]")
    action.move_to_element(secondLevelMenu).perform()

    secondLevelMenu.click()
    print(email+' created')