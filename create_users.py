from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from excel_users import extract_users



driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")

driver.get("https://dev40-na-gapinc.demandware.net/on/demandware.store/Sites-Intermix-Site/en_US/Home-Show")

#driver.get("https://dev12-na-gapinc.demandware.net/on/demandware.store/Sites-Intermix-Site/en_US/Home-Show")

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

loc = ("C:\\Users\\mkottak\\Downloads\\FireShot\\newusers.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range (127,130):
    # For row 0 and column 0
    email=sheet.cell_value(i, 0)
    firname=sheet.cell_value(i, 1)
    lasname=sheet.cell_value(i, 2)
    address1=sheet.cell_value(i, 3)
    city_val = sheet.cell_value(i, 4)
    code_val= sheet.cell_value(i, 5)
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
    input("for address:")
    driver.find_element_by_xpath("(//h2[@class='account-sub-headers'][contains(text,'')])[5]").click()
    driver.find_element_by_xpath("//a[@class='btn-secondary']").click()
    driver.implicitly_wait(5)

    idname='dwfrm_profile_address_addressid'
    fname='dwfrm_profile_address_firstname'
    lname='dwfrm_profile_address_lastname'
    add1='dwfrm_profile_address_address1'
    city='dwfrm_profile_address_city'
    code='dwfrm_profile_address_postal'
    phone='dwfrm_profile_address_phone'
    driver.find_element_by_id(idname).send_keys("Home")
    driver.find_element_by_id(fname).send_keys(firname)
    driver.find_element_by_id(lname).send_keys("OMS")
    driver.find_element_by_id(add1).send_keys(address1)

    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_id('dwfrm_profile_address_country'))
    select.select_by_visible_text('United States')



    driver.find_element_by_id(city).send_keys(city_val)

    select1 = Select(driver.find_element_by_id('dwfrm_profile_address_states_state'))
    select1.select_by_visible_text('Kansas')

    driver.find_element_by_id(code).send_keys("67401")
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