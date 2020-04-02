from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html',)

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))
    password = ''

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html',{'password':password})

def about(request):
    about_text = " Linux was the first thing I really felt excited about"
    return render(request, 'generator/about.html', {"about":about_text})
