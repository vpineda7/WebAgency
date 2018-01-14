from utils.browser.chrome import Chrome

class flightPrice():

	def get():
		Chrome().open("http://flights.ctrip.com/")
		