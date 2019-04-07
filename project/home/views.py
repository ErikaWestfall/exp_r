from django.shortcuts import render, redirect


def home(request):
    return render(request, 'temps/home.html', {'title':'Home'})
