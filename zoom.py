from pynput.mouse import Button, Controller as Mouse_Controller
from pynput.keyboard import Key, Controller as Keyboard_Controller
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
from webscreenshot import webscreenshot
from webscreenshot.webscreenshot import *
import pyscreenshot as ImageGrab
from pyscreenshot import *
from fullscreen_shot import fullpage_screenshot
from Screenshot import Screenshot_Clipping
from selenium import webdriver



options = webdriver.ChromeOptions()
#options.headless = True
#options.add_extension()

driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe",options=options)

driver.get("https://www.wikipedia.org")
#driver.get("https://dev12-na-gapinc.demandware.net/s/Intermix/customer-service/about-us/cs-terms-of-use.html")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/a").click()


"""
from Screenshot import Screenshot_Clipping
from selenium import webdriver
driver.maximize_window()
driver.execute_script("document.body.style.zoom='60%'")
driver.set_window_size(2200, 1800)
ob=Screenshot_Clipping.Screenshot()
my=1

img_url=ob.full_Screenshot(driver, save_path=r'.', image_name=str(1)+'.png')
print(img_url)
total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
print(total_height)

driver.set_window_size(2200,total_height)

time.sleep(2)
#driver.save_screenshot("screenshot1118.png")

fullpage_screenshot(driver,"screenshotmain.png")

ob=Screenshot_Clipping.Screenshot()


img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='newimage.png')
print(img_url)


#driver.quit()

from selenium.webdriver.common.action_chains import ActionChains

r=driver.find_element_by_id('main')
#t=driver.find_element_by_xpath("//div[contains(@class,'order-confirmation-details')]")
from fullscreen_shot import fullpage_screenshot
fullpage_screenshot(r ,'hi_1.png')

"""
#driver.find_element_by_xpath("//table[@role='presentation']").screenshot_as_png

driver.find_element_by_xpath("//table[@role='presentation']")
#print(h.text)

ob=Screenshot_Clipping.Screenshot()
img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='1Myimage.png')
print(img_url)


