
"""

Open Firefox browser with defined capabilities
"""

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Users\mkottak\AppData\Local\Mozilla Firefox\firefox.exe')
fp = (r'C:\Users\mkottak\AppData\Roaming\Mozilla\Firefox\Profiles\dihcdwcx.default-esr')
opts = Options()
opts.profile = fp
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
#driver=webdriver.Firefox(executable_path="C:\\Users\\mkottak\\git\\intermix\\IMX\\GAP_Intermix\\target\classes\webdriver\\geckodriver.exe")
driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, options = opts)
