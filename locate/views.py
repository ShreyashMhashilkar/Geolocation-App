from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    result = requests.get('http://ip-api.com/json/24.48.0.1')
    location = result.text
    locstion_data = json.loads(location)
    return render(request, 'index.html',{'data':locstion_data})

