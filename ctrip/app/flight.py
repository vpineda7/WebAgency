from utils.browser.chrome import Chrome
import json
import time

class flight():

	def Get(QueryString):
		chrome = Chrome()
		query = json.loads(open('config\\' + QueryString + '.json').read())

		flightsPage = json.loads(open('config\\flightsPage.json').read())		
		chrome.Open(flightsPage["URL"])

		chrome.Fill(flightsPage["FromCity"], query["FromCity"])
		time.sleep(1)
		chrome.Click(flightsPage["SearchForm"])
		
		chrome.Fill(flightsPage["ToCity"], query["ToCity"])
		time.sleep(1)
		chrome.Click(flightsPage["SearchForm"])

		chrome.Fill(flightsPage["DepartureDate"], query["DepartureDate"])
		time.sleep(1)
		chrome.Click(flightsPage["SearchForm"])

		chrome.Click(flightsPage["SearchFlight"])

		