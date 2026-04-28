from django.shortcuts import render, redirect, get_object_or_404
from django.http import  JsonResponse
from .models import *
from django.contrib import messages
import json
from .forms import *
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def home_page(request):
    brand = Brand.objects.all()
    product=Car.objects.filter(trending=1)
    return render(request,"home.html", {'brand':brand, 'product': product}) 

def about_page(request):
    return render(request, 'about.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name= request.POST.get('username')
            pwd= request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('home') 
            else:
                messages.error(request, "Invalid Username or password")
        return render(request, 'login.html') 

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect('home')

def register_Page(request):
    form = CustomUser()
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registeration Success you can Login Now!...")
            return redirect('login')
    return render(request, "register.html", {"form":form}) 

def collections_page(request):
    brands=Brand.objects.all()
    return render(request, 'collections.html', {'brands': brands})

def collections_view(request, name):
    if(Brand.objects.filter(name=name)).exists:
        cars=Car.objects.filter(brand__name=name)
        return render(request, 'carlist.html', {'cars': cars, 'brand':name})
    else:
        messages.warning(request, "No such Brands found")
        return redirect('collections') 

def cars_details(request, cname, pname):
    brand= get_object_or_404(Brand, name=cname)
    product= get_object_or_404(Car, name=pname, brand=brand)
    if request.method == 'POST':
        name= request.POST.get('username')
        mobile= request.POST.get('number')
        email= request.POST.get('email')
        if name and mobile and email :
            TestDrive.objects.create(product=product, name=name, mobile=mobile, email=email)
            messages.success(request, "Test Drive Booked Successfully")
            return redirect('car_details', cname=cname , pname=pname)
        else:
            messages.error(request, "Bookig is Problem check Out")
            return redirect('car_details',cname= cname, pname=pname) 
    return render(request, 'car_details.html',{'product': product})

def contact_page(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        phone= request.POST.get('number')
        email= request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, email=email, message=message)
        messages.success(request, "Message Sent Successfully")
        return redirect('contact')
    return render(request, 'contact.html')
    
# def fav_page(request):
#     if request.headers.get('x-requested-with')=='XMLHttpRequest':
#         if request.user.is_authenticated:
#             data=json.load(request)
#             product_id=data['pid']
#             product_status=Car.objects.get(id=product_id)
#             if product_status:
#                 if Favourite.objects.filter(user=request.user.id,product_id=product_id):
#                     return JsonResponse({'status':'Product Already in Favourite'}, status=200)
#             else:
#                 Favourite.objects.create(user=request.user,product_id=product_id)
#                 return JsonResponse({'status':'Product Added to Favourite'}, status=200)
#         else:
#             return JsonResponse({'status':'Login to Add Favourite'}, status=200)
#     else:
#         return JsonResponse({'status':'Invalid Access'}, status=200) 