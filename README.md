Project Overview

This is a Real-Time Weather App built with Python language by using its library Streamlit as a main.  
It allows users to enter a city name and get current weather conditions and 5-hour forecast using the OpenWeatherMap API.  
The app displays temperature, humidity, wind speed, pressure, dew point, and local time with weather icons.

The libarries which are used in this project are mentioned below:
streamlit: For creating the interactive web application UI.
requests: For sending HTTP requests to fetch weather data from the API.
datetime: For converting timestamps into human-readable local time.
math: For calculating the dew point using scientific formulas.

What the Project Does
Takes city name input from the user.
Fetches real-time weather and hourly forecast data from the OpenWeatherMap API.
Displays:
   Temperature (°C)
   Humidity (%)
   Wind Speed (km/h)
   Atmospheric Pressure (hPa)
   Dew Point (°C)
   Local Time of the city
   Next 5 hours forecast with icons
   Shows error messages for invalid city names or API issues. 
