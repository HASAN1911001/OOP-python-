""" -----------------------------------------------------------------------------------------------------

Use web search to find some API to get weather data. Use that to get your region's weather data every 30 minute.

Write a function named weather_data() and write your code inside this function.

-------------------------------------------------------------------------------------------------------"""

import requests, json
import schedule
import time
  
def weather():
    api_key = "8aeaab5890da9cf7baa8bbd112154f53"
    city_name = 'Dhaka'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 
    else:
        print(" City Not Found ")

def weather_data():
    schedule.every(1).minutes.do(weather)
  
    while True:
        schedule.run_pending()
        time.sleep(1)

weather_data()