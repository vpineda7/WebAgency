from utils.browser.chrome import Chrome
import os
import json
import time
from shutil import copyfile

class flight():

	def __init__(self, flightName):
		self.name = flightName
		self.flight = json.loads(open('config\\' + flightName + '.json').read())
		
	def GetMonthlyLowestPrices(self):
		chrome = Chrome()
		flightSearchPage = json.loads(open('config\\flightSearchPage.json').read())	
		flightBookingPage = json.loads(open('config\\flightBookingPage.json').read())

		### step 1
		chrome.OpenWith(flightSearchPage["URL"])

		chrome.Fill(flightSearchPage["FromCity"], self.flight["FromCity"])
		time.sleep(1)
		chrome.Click(flightSearchPage["EmptySpace"])
		
		chrome.Fill(flightSearchPage["ToCity"], self.flight["ToCity"])
		time.sleep(1)
		chrome.Click(flightSearchPage["EmptySpace"])

		chrome.Fill(flightSearchPage["DepartureDate"], self.flight["DepartureDate"])
		time.sleep(1)
		chrome.Click(flightSearchPage["EmptySpace"])

		chrome.Click(flightSearchPage["SearchFlight"])

		# nav to booking page...

		### step2
		chrome.Click(flightBookingPage["MonthlyLowPricesBtn"])
		chrome.WaitUtilVisible(flightBookingPage["LowPricesDialogData"])
		chrome.Screenshot(self.name+"_GMLP")

		# picture is stored in C:\Users\anyyu\AppData\Local\Temp\1 ...
		for file in os.listdir("C:\\Users\\anyyu\\AppData\\Local\\Temp\\1\\"):
			if file.startswith(self.name+"_GMLP"):
				copyfile("C:\\Users\\anyyu\\AppData\\Local\\Temp\\1\\"+file, "C:\\Users\\anyyu\\Documents\\MyGitRepos\\WebAgency\\ctrip\\screenshot\\"+file)


