import requests

city = input("Enter city name: ")

api_key = "155b449b7aaeb3f3c9ac0b698ec7f580"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if data["cod"] == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\nWeather Report")
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)

else:
    print("City not found")