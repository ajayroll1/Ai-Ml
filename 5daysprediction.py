#https://openweathermap.org/forecast5

import requests
from datetime import datetime

# Function to get 5-day weather forecast data
def get_weather_forecast(city_name):
    API_Key = '11bb50cc1b08e7ccb619076ee4711a06'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}&units=metric'

    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        print(f"\nWeather Forecast for {city_name}:")

        # Keep track of the last date we have seen to prevent duplicate days
        seen_dates = set()

        # Loop through the forecast data (every 3 hours, 8 times per day)
        for entry in data['list']:
            timestamp = entry['dt']
            date_time = datetime.utcfromtimestamp(timestamp)
            date_str = date_time.strftime('%Y-%m-%d')  # Only the date part (no time)

            # Only print the first forecast for each day
            if date_str not in seen_dates:
                seen_dates.add(date_str)

                # Extract forecast data for this day
                temperature = entry['main']['temp']
                weather_description = entry['weather'][0]['description']
                feels_like = entry['main']['feels_like']
                humidity = entry['main']['humidity']

                # Print the forecast data for this day
                print(f"\nDate: {date_str}")
                print(f"Weather: {weather_description.capitalize()}")
                print(f"Temperature: {temperature}°C")
                print(f"Feels Like: {feels_like}°C")
                print(f"Humidity: {humidity}%")

    else:
        print("Failed to retrieve data. Please check the city name or API key.")

# Main Function to interact with the user
def main():
    print("Welcome to the 5-Day Weather Forecast App")
    city_name = input("Enter the city name: ").strip()  # Take user input for city
    get_weather_forecast(city_name)  # Get weather forecast data for the entered city

if __name__ == '__main__':
    main()
