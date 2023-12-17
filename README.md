# Weather-Alert-App
This script is a practical and useful application, combining weather data retrieval from the OpenWeatherMap API with SMS alerts through the Twilio API. The key components are:
The Weather information app includes:
1.OpenWeatherMap API Integration: The script interacts with the OpenWeatherMap API to retrieve real-time weather information for a city. This could include details such as temperature, humidity, wind speed, and more.

2.User Input: The user is prompted to input a city, suggesting that the script is designed to fetch weather information for a specific location based on user preference.

3. Output: The weather description and temperature in celcius is given out as output.
 
The second part of this project is "The Waether Alert App", I added a few more features to "Weather Information App" which is as follows:

4.Twilio API Integration: The Twilio API is utilized to send SMS alerts. This implies that the script has the ability to determine and analyze weather conditions and trigger SMS alerts in response to drastic changes.

5.Automation with PythonAnywhere: PythonAnywhere is used to automate the Python script, suggesting that this weather monitoring and alert system can run periodically in a cloud-based environment. 
We can schedule this script to run everyday in the morning, the script is designed to check the the weather data of next twelve hours, and if it finds a possiblity of rain (i.e. weather id< 700) it send SMS to alert that "It may rain, so bring an umbrella!" 

