from splinter import Browser

#Need to put the chrome driver in C disk
executable_path = {'executable_path':'C:\Google\chromedriver.exe'}

browser = Browser('chrome', **executable_path)

# Enter 12306 login page
browser.visit('https://kyfw.12306.cn/otn/index/init')
login_button = browser.find_by_id('login_user')
login_button.click()

# Type login informations
username_input = browser.find_by_id('username')
username_input.fill('yay00yay')

psw_input = browser.find_by_id('password')
psw_input.fill('307317yu')

# Wait for use to select login pictures and finish login
print (browser.is_element_present_by_text("余安阳", wait_time=60))

# Select booking button
booking_button = browser.find_by_id('selectYuding')
booking_button.click()

# fill start/end stations and start date
fromStationtInput = browser.find_by_id("fromStationText")
fromStationtInput.click()
fromStationtInput.fill("北京西")
exactlyStationItem = browser.find_by_id("citem_0")
exactlyStationItem.click();

toStationtInput = browser.find_by_id("toStationText")
toStationtInput.click()
toStationtInput.fill("宜昌东")
exactlyStationItem = browser.find_by_id("citem_0")
exactlyStationItem.click();