from django.shortcuts import render
from decouple import config
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST' and request.POST:
        city = request.POST['city']
        send = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+config('OPEN_W_API')+'&units=metric').read()
        resJSON = json.loads(send)
        data = {
            "country_code": str(resJSON['sys']['country']),
            "coordinate": 'X '+str(resJSON['coord']['lon'])+ ' Y '+str(resJSON['coord']['lat']),
            "temp": str(resJSON['main']['temp'])+' C'+u"\N{DEGREE SIGN}",
            "pressure": str(resJSON['main']['pressure']),
            "humidity": str(resJSON['main']['humidity']),
        }
    else:
        city = ' '
        data = {}
    return render(request,'index.html', {'city':city, 'data':data})

def page_not_found(request, exception):
    return render(request, '404.html', status=404)