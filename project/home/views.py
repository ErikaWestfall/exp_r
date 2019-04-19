from django.shortcuts import render, redirect

def home(request):
    u = request.user
    context = {'u': u, 'title':'Home'}
    return render(request, 'temps/home.html', context)

