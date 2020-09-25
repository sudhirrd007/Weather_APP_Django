from django.shortcuts import render
import requests
# get your API KRY and changed with below key
api_key = '243be12ced24cc2a61ec4f13e258d2a4'

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='+api_key
    city = "Las Vegas"
    city_weather = requests.get(url.format(city)).json()

    weather = {
        "city": city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {"weather":weather}

    return render(request, 'app/index.html', context=context)