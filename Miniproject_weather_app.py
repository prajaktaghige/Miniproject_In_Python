import requests # type: ignore

def get_weather(city):
    api_key = 'your_api_key_here'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get('cod') != 200:
        print("City not found.")
    else:
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
