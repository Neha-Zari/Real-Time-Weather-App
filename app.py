import streamlit as st
import requests
from datetime import datetime
import math

API_KEY = "2e2e060bc01327b21aff1e60a0f24b8d"

st.set_page_config(page_title="🌤️ Real-Time Weather", layout="centered")
st.title("🌤️Weather App")

city = st.text_input("Enter City Name", "").strip()

def calculate_dew_point(temp_c, humidity):
    a = 17.27
    b = 237.7
    alpha = ((a * temp_c) / (b + temp_c)) + math.log(humidity / 100.0)
    dew_point = (b * alpha) / (a - alpha)
    return round(dew_point, 2)

def format_time(timestamp, offset):
    local_time = datetime.utcfromtimestamp(timestamp + offset)
    return local_time.strftime("%I:%M %p")

if city:

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code == 200 and forecast_response.status_code == 200:
        data = weather_response.json()
        forecast_data = forecast_response.json()

        st.success(f" Weather in {city.title()}")

        weather = data["weather"][0]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        icon_code = weather["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        description = weather["description"].title()
        dew_point = calculate_dew_point(temp, humidity)

        timezone_offset = data["timezone"]
        local_time = datetime.utcfromtimestamp(data["dt"] + timezone_offset)
        formatted_time = local_time.strftime("%A, %d %B %Y %I:%M %p")

        col_icon, col_temp = st.columns([1, 3])
        with col_icon:
            st.image(icon_url, width=80)
        with col_temp:
            st.metric("🌡️ Temperature", f"{temp} °C")

        st.markdown(f"**🌥️ Weather Condition:** {description}")
        st.markdown(f"**:** {formatted_time}")

        col1, col2 = st.columns(2)
        col1.metric("💧 Humidity", f"{humidity}%")
        col2.metric("💨 Wind Speed", f"{wind_speed} km/h")

        col3, col4 = st.columns(2)
        col3.metric("📈 Pressure", f"{pressure} hPa")
        col4.metric("🌫️ Dew Point", f"{dew_point} °C")

        st.markdown("---")
        st.subheader("🕒 Hourly Forecast (Next 5 Hours)")

        forecast_list = forecast_data["list"]
        count = 0

        for hour_data in forecast_list:
            forecast_time = hour_data["dt"]
            hour_local = format_time(forecast_time, timezone_offset)

            forecast_temp = hour_data["main"]["temp"]
            forecast_desc = hour_data["weather"][0]["description"].title()
            icon_code = hour_data["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

            with st.container():
                col1, col2, col3 = st.columns([1, 2, 3])
                with col1:
                    st.image(icon_url, width=60)
                with col2:
                    st.write(f"**{hour_local}**")
                    st.write(f"{forecast_desc}")
                with col3:
                    st.metric(label="🌡️ Temp", value=f"{forecast_temp} °C")

            count += 1
            if count >= 5:
                break

    elif weather_response.status_code == 404:
        st.error("❌ Invalid city name. Please try again.")
    else:
        st.error("⚠️ Unable to fetch data. Try again later.")
