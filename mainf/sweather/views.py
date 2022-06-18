from django.shortcuts import render
from decouple import config
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        send = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+config('OPEN_W_API')).read()
        resJSON = json.loads(send)
        data = {
            "country_code": str(resJSON['sys']['country']),
            "coordinate": str(resJSON['coord']['lon'])+ ' '+str(resJSON['coord']['lat']),
            "temp": str(resJSON['main']['temp'])+'k',
            "pressure": str(resJSON['main']['pressure']),
            "humidity": str(resJSON['main']['humidity']),
        }
    else:
        city = ' '
        data = {}
    return render(request,'index.html', {'city':city, 'data':data})
    