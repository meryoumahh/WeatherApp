from django.shortcuts import render
import json 
import urllib.request
# Create your views here.
def index(request):
    """
    Render the index page of the weather detector app.
    """
    if request.method == 'POST':
        # Handle form submission or other POST logic here
        city = request.POST.get('city')
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a5b1d4af5726e8af7ac860098c6082b6').read()
        json_data = json.loads(res)
        data = {
            'city': city,
            'country_code': str( json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'] )+ 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
            
        }
    else:
        # Default city or initial data
        data = {}
    return render(request, 'index.html', {'data': data})