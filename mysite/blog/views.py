from django.shortcuts import render

def home(request):

    testo = request.POST.get('testo')
    numero = request.POST.get('numero')

    context = {
        'messaggio': 'Benvenuto nella homepage!',
        'testo':testo,
        'numero':numero
    }

    return render(request, 'home.html', context)
