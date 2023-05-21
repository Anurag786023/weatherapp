from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    city=request.GET.get('city_name','lucknow')

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ea5a0e708125ad4bd642e5684f6f7f09'
    data=requests.get(url).json()
   
    payload={
        'city': data["name"],"weather":data['weather'][0]['main'],'temp_k':int(data['main']['temp']),'temp_c':int(data['main']['temp'])-273,'presure':data['main']['pressure'],'humidity':data['main']['humidity']
    }
    context={
        'data':payload
    }
    # print(context)
    
    return render(request,"home.html",context)
