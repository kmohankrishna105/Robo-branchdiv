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


driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")
driver.get("https://www.wikipedia.org")

driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "-")