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
import xlrd
from selenium.webdriver import DesiredCapabilities
#import firefox
loc = ("C:\\Users\\mkottak\\Downloads\\FireShot\\place.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


driver = webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")
#driver = webdriver.Ie(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\IEDriverServer.exe")
#####driver = webdriver.Firefox(executable_path="C:\\Users\\mkottak\\git\\intermix\\IMX\\GAP_Intermix\\target\classes\webdriver\\geckodriver.exe",capabilities=cap,firefox_binary=binary)
#driver=firefox.driver

"""
preorder1_url = 'https://dev12-na-gapinc.demandware.net/s/Intermix/faithfull-the-brand/brigit-mini-dress/6000300198.html'
preorder2_url = 'http://dev12-na-gapinc.demandware.net/s/Intermix/rag-bone%2Fjean/floral-vintage-tee/6000085244.html'
cart_url = 'https://dev12-na-gapinc.demandware.net/s/Intermix/cart'
normal1_url = "http://dev12-na-gapinc.demandware.net/s/Intermix/intermix/aisley-knit-cami/8888341964.html"
normal2_url = "http://dev12-na-gapinc.demandware.net/s/Intermix/hansel-from-basel/back-seam-tulle-sheer-socks/6000375190.html"


preorder1_url = 'https://development-sfcc.intermixonline.com/on/demandware.store/Sites-Intermix-Site/en_US/Product-Variation?pid=93570G&dwvar_93570G_size=70&dwvar_93570G_color=020'
preorder2_url = 'https://development-sfcc.intermixonline.com/on/demandware.store/Sites-Intermix-Site/en_US/Product-Variation?pid=93570G&dwvar_93570G_size=70&dwvar_93570G_color=020'
cart_url = 'https://development-sfcc.intermixonline.com/cart'
normal1_url = "https://development-sfcc.intermixonline.com/on/demandware.store/Sites-Intermix-Site/en_US/Product-Variation?pid=93570G&dwvar_93570G_size=70&dwvar_93570G_color=020"
normal2_url = "https://development-sfcc.intermixonline.com/on/demandware.store/Sites-Intermix-Site/en_US/Product-Variation?pid=93570G&dwvar_93570G_size=70&dwvar_93570G_color=020"
"""

preorder1_url = 'https://dev40-na-gapinc.demandware.net/s/Intermix/faithfull-the-brand/brigit-mini-dress/6000300198.html'
preorder2_url = 'http://dev40-na-gapinc.demandware.net/s/Intermix/rag-bone%2Fjean/floral-vintage-tee/6000085244.html'
cart_url = 'https://dev40-na-gapinc.demandware.net/s/Intermix/cart'
normal1_url = "http://dev40-na-gapinc.demandware.net/s/Intermix/intermix/aisley-knit-cami/8888341964.html"
normal2_url = "http://dev40-na-gapinc.demandware.net/s/Intermix/hansel-from-basel/back-seam-tulle-sheer-socks/6000375190.html"

driver.get(cart_url)

print("hai")
input("Whats next")
driver.maximize_window()

"""
height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(900,height+6000)
driver.save_screenshot("image.png")
"""

driver.find_element_by_xpath("//a[@title='User: My Account']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[contains(@id,'dwfrm_login_username')]").send_keys('159oms@yopmail.com')
driver.find_element_by_xpath("//input[contains(@id,'dwfrm_login_password')]").send_keys("Test@123")
driver.find_element_by_name("dwfrm_login_login").click()


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(preorder1_url)
driver.maximize_window()

"""
height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(900,height+700)
driver.save_screenshot("image2.png")
"""


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get(preorder2_url)

"""
from selenium.common.exceptions import TimeoutException
try:

    alert = driver.switch_to.alert
    alert.accept()
    print("alert accepted")
except :
    pass
"""

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get(normal1_url)


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])
driver.get(normal2_url)


for i in range (0,6):
    # For row 0 and column 0
    q1=sheet.cell_value(i, 0)
    q2=sheet.cell_value(i, 1)

    q3=sheet.cell_value(i, 2)
    q4=sheet.cell_value(i, 3)
    card_details = sheet.cell_value(i, 4)
    #gift_card= sheet.cell_value(i, 5)
    img_name=sheet.cell_value(i, 6)
    gift_details1=sheet.cell_value(i, 7)
    ship_method = sheet.cell_value(i, 9)
    gift_details3 = sheet.cell_value(i, 11)
    pin_details1 = sheet.cell_value(i, 8)
    pin_details2 = sheet.cell_value(i, 10)
    pin_details3 = sheet.cell_value(i, 12)
    coupon=sheet.cell_value(i,5)



    if q1!="":
        driver.switch_to.window(driver.window_handles[1])
        select1 = Select(driver.find_element_by_id('product-qty'))
        select1.select_by_visible_text(str(int(q1)))
        driver.find_element_by_id("add-to-cart").click()

    if q2!="":
        driver.switch_to.window(driver.window_handles[2])
        select1 = Select(driver.find_element_by_id('product-qty'))
        select1.select_by_visible_text(str(int(q2)))
        driver.find_element_by_id("add-to-cart").click()

    if q3!="":
        driver.switch_to.window(driver.window_handles[3])
        try:
            driver.find_element_by_xpath("//div[@class='push-close']").click()
        except:
            pass
        select1 = Select(driver.find_element_by_id('product-qty'))
        select1.select_by_visible_text(str(int(q3)))
        driver.find_element_by_id("add-to-cart").click()

    if q4!="":
        driver.switch_to.window(driver.window_handles[4])
        try:
            driver.find_element_by_xpath("//div[@class='push-close']").click()
        except:
            pass
        select1 = Select(driver.find_element_by_id('product-qty'))
        select1.select_by_visible_text(str(int(q4)))
        driver.find_element_by_id("add-to-cart").click()

    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(8)
    driver.find_element_by_class_name("minicart-quantity").click()

    driver.find_element_by_id("dwfrm_cart_couponCode").send_keys(str(coupon))
    driver.find_element_by_id("add-coupon").click()


    #input("Place order:")

    try:
        driver.implicitly_wait(1)
        driver.find_element_by_name("dwfrm_cart_checkoutCart").click()
        driver.implicitly_wait(5)

        driver.find_element_by_xpath("//input[contains(@id,'dwfrm_billing_paymentMethods_creditCard_number')]").send_keys(str(card_details))

        month = Select(driver.find_element_by_id('dwfrm_billing_paymentMethods_creditCard_expiration_month'))
        month.select_by_visible_text('10 October')

        year = Select(driver.find_element_by_id('dwfrm_billing_paymentMethods_creditCard_expiration_year'))
        year.select_by_visible_text('2020')

        driver.find_element_by_xpath("//input[contains(@id,'dwfrm_billing_paymentMethods_creditCard_cvn')]").send_keys(
            '737')
    except:
        input("Credit card issue")
        pass


    try:
        driver.find_element_by_xpath("//button[@name='dwfrm_billing_save']").click()

        shipmethod = Select(driver.find_element_by_xpath("//select[@id='shipping-method-list']"))

        shipmethod.select_by_visible_text(str(ship_method))
    except:
        input("Save button issue")
        pass



    try:
        if gift_details1 != "":
            apply_gift_card = "//button[@class ='gift-cert-link btn-flat']"
            driver.find_element_by_xpath(apply_gift_card).click()
            #driver.find_element_by_xpath("//label[@for='dwfrm_billinggiftcert_giftCertCode']/span").clear()
            elem = driver.find_element_by_xpath("//label[@for='dwfrm_billinggiftcert_giftCertCode']/span")
            actions = ActionChains(driver)
            actions.move_to_element(elem)
            actions.click()
            actions.send_keys(str(gift_details1))
            actions.perform()
            #driver.find_element_by_xpath("//label[@for='dwfrm_billinggiftcert_giftCertCode']/span").send_keys(str(gift_details1))
            elem_pin=driver.find_element_by_id("dwfrm_billinggiftcert_giftCertPin")
            actions1 = ActionChains(driver)
            actions1.move_to_element(elem_pin)
            actions1.click()
            actions1.send_keys(str(pin_details1))
            actions1.perform()
            driver.implicitly_wait(4)
            #driver.find_element_by_id("dwfrm_billinggiftcert_giftCertPin").send_keys(str(pin_details1))
            #input("card1")
            driver.find_element_by_xpath("//div/button[@id='add-giftcert']").click()
            #input("Tconfirm gift card")
    except:
        input("Gift card issue")

    #input("make changes")

    driver.find_element_by_xpath("//button[@value='Place Order']").click()
    driver.implicitly_wait(5)



    time.sleep(4)

    from Screenshot import Screenshot_Clipping
    driver.save_screenshot(str(img_name) + 'm.png')
    driver.execute_script("document.body.style.zoom='50%'")
    # driver.set_window_size(2200, 1800)
    driver.save_screenshot(str(img_name)+'.png')
    ob = Screenshot_Clipping.Screenshot()

    img_url = ob.full_Screenshot(driver, save_path=r'.', image_name=str(img_name)+'.png')
    print(img_url)
    driver.execute_script("document.body.style.zoom='80%'")
    driver.save_screenshot(str(img_name)+'_80.png')


    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    print(total_height)

    driver.set_window_size(2200, total_height)
    #input("Take screen shots")
    time.sleep(2)
    try:
        f=driver.find_element_by_xpath("//div[@class='order-number']//span[2]")
        print(img_name+' -- ' +f.text)
    except:
        input("End of order:")
    input("verify next order")


