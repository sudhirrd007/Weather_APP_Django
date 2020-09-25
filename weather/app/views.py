from django.shortcuts import render
import requests
from app.models import City
from app.forms import CityForm

# get your API KRY and changed with below key
api_key = '243be12ced24cc2a61ec4f13e258d2a4'

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid='+api_key
    cities = City.objects.all() # return all the cities in the DB
    
    if(request.method == "POST"): # Only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []
    city_names = []

    for city in cities:
        if(city.name in city_names):
            city.delete()
        else:
            city_names.append(city.name)
            city_weather = requests.get(url.format(city)).json()
            if(city_weather["cod"] != "404"):
                weather = {
                    "city": city,
                    'temperature' : city_weather['main']['temp'],
                    'description' : city_weather['weather'][0]['description'],
                    'icon' : city_weather['weather'][0]['icon']
                }
                weather_data.append(weather)
            else:
                city.delete()

    context = {"weather_data" : weather_data, "form": form}

    return render(request, 'app/index.html', context=context)