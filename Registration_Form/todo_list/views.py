from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse


from .models import User
from django.contrib import messages


import time

from django.core.cache import cache
from django.http import JsonResponse
cache.clear()


email = "aa"


def welcome(request):
    return render(request, 'welcome.html', {"title": "Home"})


def signup_view(request):
    print("call")
    if request.method == "POST":
        d = {}
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        dob = request.POST.get("dob")
        print(name, email, mobile, dob)
        try:
            user = User(Name=name, Email=email, Mobile=mobile, dob=dob)
            user.save()
            d['status'] = 1
            d['name'] = name
            d['email'] = email
            d['mobile'] = mobile
            d['dob'] = dob

            # return render(request, 'home.html',{'username':name})
        except Exception as e:
            print(e)
            d['status'] = 0

    return JsonResponse(d, safe=False)


def data_view(request):
    data = {}
    user = User.objects.filter().values()
    data['user_data'] = list(user)
    return JsonResponse(data, safe=False)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(Email=username).first()
        if user:
            if user.Password == password:
                request.session['user'] = username
                return render(request, 'home.html', {'username': user.Name})

            else:
                return render(request, 'welcome.html', {"error": "invalid password"})
        else:
            return render(request, 'welcome.html', {"error": "Invalid mobile"})
    return render(request, 'welcome.html', {"error": "Invalid mobile"})


def home(request):
    if request.method == 'POST':
        # form = ListForm(request.POST or None)
        # if form.is_valid():
        #     form.save()
        all_items = list.objects.all
        messages.success(request, ('Item has been added to List'))
        return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request):
    data = {}
    id = request.GET.get("id")
    try:
        User.objects.filter(id=id).delete()
        data['status'] = 1
    except:
        data['status'] = 0

    return JsonResponse(data, safe=False)
