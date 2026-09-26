import requests
from datetime import datetime

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    data = requests.get(API_URL)
    if data.status_code == 200:
        return data.json()
    else:
        print("Some Problem occured while fetching the  weather data")
        return None

def get_temperature(date):
    weather_data = get_weather_data()
    if weather_data:
        for entry in weather_data["list"]:
            if date in entry["dt_txt"]:
                return entry["main"]["temp"]
        print("Date not found in the forecast.")
        return None

def get_wind_speed(date):
    weather_data = get_weather_data()
    if weather_data:
        for entry in weather_data["list"]:
            if date in entry["dt_txt"]:
                return entry["wind"]["speed"]
        print("Date not found in the forecast.")
        return None

def get_pressure(date):
    weather_data = get_weather_data()
    if weather_data:
        for entry in weather_data["list"]:
            if date in entry["dt_txt"]:
                return entry["main"]["pressure"]
        print("Date not found in the forecast.")
        return None

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

def main():
    while True:
        print("Menu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date in (yyyy-mm-dd hh:mm:ss) format: ")
            if not validate_date_format(date):
                print("Invalid date format.")
                continue

            temperature = get_temperature(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}K \n")

        elif choice == "2":
            date = input("Enter the date in (yyyy-mm-dd hh:mm:ss) format: ")
            if not validate_date_format(date):
                print("Invalid date format.")
                continue

            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s\n")

        elif choice == "3":
            date = input("Enter the date  in (yyyy-mm-dd hh:mm:ss) format: ")
            if not validate_date_format(date):
                print("Invalid date format.")
                continue

            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa\n")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
