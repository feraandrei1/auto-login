from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

###########################################################

#enter the link to the website you want to automate login.
website_link="https://github.com/login"

#enter login credentials
username = "your_username"
password = "your_password"

###########################################################

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
# browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]

browser = webdriver.Chrome()	#uncomment this line,for chrome users
browser.get((website_link))

try:
	
	username_element = browser.find_element("id", "login_field")
	username_element.send_keys(username)		
	password_element  = browser.find_element("id", "password")
	password_element.send_keys(password)
	signInButton = browser.find_element("name", "commit")
	signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	time.sleep(999)
	browser.quit()
	
	#### to quit the browser uncomment the following lines ####
	# time.sleep(999)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)

except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print("Some error occured :(")

	#### to quit the browser uncomment the following lines ####
	# browser.quit()
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)