from django.shortcuts import render

def home(request):
    context = {
        'messaggio': 'Benvenuto nella homepage!'
    }

    return render(request, 'home.html', context)
