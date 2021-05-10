import requests
import json

locDef = {294:"BBMP",265:"Bangalore Urban"} 

def sendMessage(avaialbility):
	messageURL = 'https://api.telegram.org/bot1822788195:AAFx5kpYzVb7Xxv1LYDkFqOxjjb8MiohREs/sendMessage?chat_id=-1001222762503&text='+ avaialbility
	requests.get(messageURL)
	
def checkAvailability(district_id,date):
	dataURL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
	PARAMS = {'district_id':district_id,'date':date}
	response = requests.get(url = dataURL, params = PARAMS)
	checkResponse(response,district_id,date)
	
def checkResponse(response,district_id,date):
	#print(response)
	#dict = open("data.json")
	#f = open('data.json','r')
	#dict = json.load(f)
	centers = response['centers']
	for center in centers:
		session = center['sessions']
		for s in session:
			if(s['vaccine'] == 'COVAXIN'):
				if(s['available_capacity'] > 0):
					messageString = " Available in " + locDef[district_id]+ ' -- ' + center['name'] + " for date "+ s['date']
					sendMessage(messageString)


locations = [294,265]
dates = ["09-05-2021", "16-05-2021", "23-05-2021"]

for loc in locations:
	for date in dates:
		checkAvailability(loc,date)				
