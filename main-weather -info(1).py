import requests

api_key="your api key"
#the endpoints that we will be using.
Geocode_endpt="http://api.openweathermap.org/geo/1.0/direct"
OWM_Endpoint= "https://api.openweathermap.org/data/2.5/weather"

##taking the city name as the user input.
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
#print(weather_data1)

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
#Priinting the weather details and temperature in celcius.
print(weather_data["weather"][0]["description"])
print(int(weather_data["main"]["temp"])-273)








    

