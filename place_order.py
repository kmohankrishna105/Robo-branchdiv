from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from excel_users import extract_users
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import openpyxl
loc = ("C:\\Users\\mkottak\\Downloads\\FireShot\\newusers.xls")


"""
wb = openpyxl.load_workbook(loc)
sheet = wb

for i in range (0,1):
    # For row 0 and column 0
    q1=sheet.cell_value(i, 0)
    q2=sheet.cell_value(i, 1)
    q3=sheet.cell_value(i, 2)
    q4=sheet.cell_value(i, 3)
    card_details = sheet.cell_value(i, 4)
    gift_card= sheet.cell_value(i, 5)
    #print(email)
"""

driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")


preorder1_url='https://dev12-na-gapinc.demandware.net/s/Intermix/alexander-wang/attica-mini-fanny-bag/6003550621.html'
preorder2_url='https://dev12-na-gapinc.demandware.net/s/Intermix/faithfull-the-brand/brigit-mini-dress/6000300198.html'
cart_url='https://dev12-na-gapinc.demandware.net/s/Intermix/cart'
normal1_url="https://dev12-na-gapinc.demandware.net/s/Intermix/galvan/asymmetric-bias-cut-dress/8888351405.html"
normal2_url="https://dev12-na-gapinc.demandware.net/s/Intermix/galvan/sash-neck-satin-gown/6000205200.html"


driver.get(cart_url)


import page_screenshot

page_screenshot



driver.maximize_window()

driver.find_element_by_xpath("(//span)[12]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[contains(@id,'dwfrm_login_username')]").send_keys('49oms@yopmail.com')
driver.find_element_by_xpath("//input[contains(@id,'dwfrm_login_password')]").send_keys("Test@123")
driver.find_element_by_name("dwfrm_login_login").click()



driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(preorder1_url)


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get(preorder2_url)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get(normal1_url)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])
driver.get(normal2_url)

select1 = Select(driver.find_element_by_id('product-qty'))
select1.select_by_visible_text('4')
driver.find_element_by_id("add-to-cart").click()

driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_class_name("minicart-quantity").click()

driver.find_element_by_id("dwfrm_cart_couponCode").send_keys("20percent")
driver.find_element_by_id("add-coupon").click()
driver.find_element_by_name("dwfrm_cart_checkoutCart").click()


driver.find_element_by_xpath("//input[contains(@id,'dwfrm_billing_paymentMethods_creditCard_number')]").send_keys('5555444433331111')

month = Select(driver.find_element_by_id('dwfrm_billing_paymentMethods_creditCard_expiration_month'))
month.select_by_visible_text('10 October')


year = Select(driver.find_element_by_id('dwfrm_billing_paymentMethods_creditCard_expiration_year'))
year.select_by_visible_text('2020')

driver.find_element_by_xpath("//input[contains(@id,'dwfrm_billing_paymentMethods_creditCard_cvn')]").send_keys('737')

driver.find_element_by_xpath("//button[@id='billingSubmitButton']").click()

shipmethod = Select(driver.find_element_by_xpath("//select[@id='shipping-method-list']"))

shipmethod.select_by_visible_text('2nd Day Air (2 business days) $25')

driver.find_element_by_xpath("//button[@value='Place Order']").click()
driver.implicitly_wait(5)
"""
ele=driver.find_element("xpath", '//div[@class="react-grid-layout layout"]')
total_height = ele.size["height"]+1000

driver.set_window_size(1920, total_height)

"""
time.sleep(2)
driver.save_screenshot("screenshot1.png")


input("Whats next")



"""


# open tab
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+'t')
#preorder1 = driver.window_handles[1]
cart = driver.window_handles[0]
#cart = driver.switch_to.default_content()
#driver.switch_to.window(preorder1)
#driver.get(preorder1_url)
print(driver.title)
driver.switch_to.window(cart)
print(driver.title)

"""
