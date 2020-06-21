from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,"generator/home.html")

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    numbers = list('0123456789')  
    password = ''
    special_chars = list('!/?^%$#@()|')  
    upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if request.GET.get('uppercase'):
        characters.extend(upper_characters)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special_chars)

    for x in range(length):
        password+=random.choice(characters)

    return render(request,"generator/password.html",{'password':password})