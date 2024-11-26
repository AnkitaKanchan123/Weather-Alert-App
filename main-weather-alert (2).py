import requests
from twilio.rest import Client

account_sid = 'Your ccount_sid'
auth_token = 'Your auth_token'

api_key="YOUR API KEY"
#the endpoints that we will be using.
Geocode_endpt="http://api.openweathermap.org/geo/1.0/direct"
OWM_Endpoint= "https://api.openweathermap.org/data/2.5/forecast"

#taking the city name as the user input.
city=input()
#parameter for the Geocode api call.
weather_params1={
    "q":city,
    "limit":1,
    "appid":api_key,
}
#creating a request to geocode api.
response1=requests.get(Geocode_endpt,params=weather_params1)
response1.raise_for_status()
weather_data1 = response1.json()

#parameter for the "5 Day / 3 Hour Forecast" api call.
weather_params ={
    "lat":weather_data1[0]["lat"],
    "lon":weather_data1[0]["lon"],
    "appid":api_key,
    "cnt":4,
}
#creating a request to "5 Day / 3 Hour Forecast" api.
response =requests.get(OWM_Endpoint , params=weather_params)
response.raise_for_status()
weather_data = response.json()

#print(weather_data)
"""for hr_data in weather_data["list"]:
    weather_id = hr_data["weather"][0]["id"]
    print(weather_id)
for hr_data in weather_data["list"]:
    if int(hr_data["weather"][0]["id"])< 700 :
        print("It may rain, bring umbrella!")
        break"""
#using twilio to create a client and send SMS to the users.
for hr_data in weather_data["list"]:
    if int(hr_data["weather"][0]["id"]) < 700 :
       client = Client(account_sid, auth_token)
       message = client.messages.create(
       from_='TWILIO NUMBER',
       body='It may rain, so bring an umbrella!',
       to='YOUR NUMBER'
       )
       print(message.status)
       """The message.status will give you the status of the sent message,
       which can be values like "queued," "sending," "sent," "failed," etc."""
       break




    

