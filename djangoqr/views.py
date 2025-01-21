from django.shortcuts import render, redirect
from .forms import QrForm, UserRegistrationForm
import qrcode
import os
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView



#Home page render
# def home(request):
#     return render(request, 'home.html')


#geenrate QR code page
@login_required
def generate_qr_code(request):
    qr_url = None
    qr_file = None
    file_name = None

    if request.method == 'POST':
        form = QrForm(request.POST, request.FILES)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant']
            url = form.cleaned_data['url']
            file = form.cleaned_data['file']
        
            # QR Code Generation
            if url:
                qr = qrcode.make(url)
                file_name = res_name.replace(" ","_").lower() + ".png"
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                qr.save(file_path)
                qr_url = os.path.join(settings.MEDIA_URL, file_name)
            elif file:
                file_extension = file.name.split('.')[-1].lower()
                file_name = res_name.replace(" ", "_").lower() + "_file." + file_extension
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            
                # Saving the uploaded file (pdf, excel, csv)
                with open(file_path, 'wb') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                        
                # Generating QR for the uploaded file
                file_url = os.path.join(settings.MEDIA_URL, file_name)
                qr = qrcode.make(file_url)
                qr_file_name = res_name.replace(" ","_").lower() + "_qr.png"
                qr_file_path = os.path.join(settings.MEDIA_ROOT, qr_file_name)
                qr.save(qr_file_path)
                qr_url = os.path.join(settings.MEDIA_URL, qr_file_name)
                qr_file = qr_url
            
            context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
                'qr_file': qr_file
            }
            return render(request, 'qr_result.html', context)

    else:
        form = QrForm()

    context = {
        'form': form,
    }
    return render(request, 'generate_qr_code.html', context)


def Register(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('generate_qr_code')
    else:
        form = UserRegistrationForm()   
    return render(request, 'register.html', {'form':form})   



#Weather App API fetch





def home(request):
    city = request.GET.get('city','lucknow').lower()
    api_key ='5367608ab1bd1d50bc2daa5560cc1fd2'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    API_KEY = 'AIzaSyDhj9_GVAyD99uzOWpBu6NsjOFEi-50ziQ'
    SEARCH_ENGINE_ID = '2125e1a990eab428c'
    
    query = city + "1920x1080"
    page = 1
    start = (page-1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    #count = 1
    search_items = data.get('items')
    image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'
    
    
    image_url = "https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600"  # Fallback image URL
    try:
        data = requests.get(city_url).json()
        print("city image: ",data)
        search_items = data.get('items', [])
        if search_items and len(search_items) > 1:
            link = search_items[1].get('link')
            if link and link.startswith('http'):
                image_url = link
                print(data)
    except Exception as e:
        print(f"Error fetching city image: {e}")
        image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'
    
    
    weather_data = {}
    error_message = None
    icon = None
    
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        icon = data['weather'][0]['icon']
                
        weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'day' : datetime.datetime.now().strftime("%d/%m/%Y")
                
        }
        
    except requests.exceptions.RequestException:
        error_message = "Unable to fetch weather data. Please try again later."
        
    return render(request, 'home.html', {'weather_data':weather_data, 'error_message':error_message, 'icon':icon, 'image_url':image_url})




def merge_pdf(request):
    return render(request, 'mergepdf.html')