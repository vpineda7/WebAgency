from splinter import Browser
import time

#personal information
_usernickname = 'yay00yay'
_userrealname = "余安阳"
_userpassword = '307317yu'

_fromStationName = "苏州"
_toStationName = "宜昌东"
_ticketTag = "ticket_550000D95600"

#Need to put the chrome driver in C disk
executable_path = {'executable_path':'C:\Google\chromedriver.exe'}
browser = Browser('chrome', **executable_path)

# Enter 12306 login page
browser.visit('https://kyfw.12306.cn/otn/index/init')
login_button = browser.find_by_id('login_user')
login_button.click()

# Type login informations
username_input = browser.find_by_id('username')
username_input.fill(_usernickname)

psw_input = browser.find_by_id('password')
psw_input.fill(_userpassword)

# Refresh Pictures
refresh_btn = browser.find_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[1]')
refresh_btn.click()

# Wait for use to select login pictures and finish login
print (browser.is_element_present_by_text(_userrealname, wait_time=60))

# Select booking button
booking_button = browser.find_by_id('selectYuding')
booking_button.click()

# fill start/end stations and start date
fromStationtInput = browser.find_by_id("fromStationText")
fromStationtInput.click()
fromStationtInput.fill(_fromStationName)
exactlyStationItem = browser.find_by_id("citem_0")
exactlyStationItem.click();

toStationtInput = browser.find_by_id("toStationText")
toStationtInput.click()
toStationtInput.fill(_toStationName)
exactlyStationItem = browser.find_by_id("citem_0")
exactlyStationItem.click();

while False == browser.is_element_present_by_id('submitOrder_id', wait_time=None):
	if True == browser.is_element_present_by_id(_ticketTag, wait_time=None):
		# check if the ticket has a button to click		
		if browser.is_element_present_by_xpath('//*[@id="'+_ticketTag+'"]/td[13]/a'):		
			browser.find_by_xpath('//*[@id="'+_ticketTag+'"]/td[13]/a').click()
		else:
			browser.find_by_id('query_ticket').click()
	else:
		# Page is not loaded...
		time.sleep(0.5)