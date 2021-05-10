import requests
import json

locDef = {294:"BBMP",265:"Bangalore Urban"} 

def sendMessage(avaialbility):
	messageURL = 'https://api.telegram.org/bot1822788195:AAFx5kpYzVb7Xxv1LYDkFqOxjjb8MiohREs/sendMessage?chat_id=-1001222762503&text='+ avaialbility
	requests.get(messageURL)
	
def checkAvailability(district_id,date):
	dataURL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
	PARAMS = {'district_id':district_id,'date':date}
	headers = {
 		'Host': 'cdn-api.co-vin.in',
 		'Accept': 'application/json',
 		'Accept-Encoding': 'application/json',
 		'Connection': 'keep-alive',
 		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}
	response = requests.get(url = dataURL, params = PARAMS, headers= headers)
	checkResponse(response,district_id,date)
	
def checkResponse(response,district_id,date):
	json_response = response.json()
	centers = json_response['centers']
	for center in centers:
		session = center['sessions']
		for s in session:
			if(s['vaccine'] == 'COVAXIN'):
				if(s['available_capacity'] > 0):
					messageString = " Available in " + locDef[district_id]+ ' -- ' + center['name'] + ' with zipcode : '+center['pincode']+ " for date "+ s['date']
					#print(messageString)
					sendMessage(messageString)


locations = [294,265]
dates = ["09-05-2021", "16-05-2021", "23-05-2021"]

for loc in locations:
	for date in dates:
		checkAvailability(loc,date)				
