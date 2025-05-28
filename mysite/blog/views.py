from django.shortcuts import render

def home(request):

    testo = request.POST.get('testo')
    numero = request.POST.get('numero')

    context = {
        'messaggio': 'Benvenuto nella homepage!',
        'testo':testo,
        'numero':numero
    }

    return render(request, 'indice.html', context)

def indice(request):
    return render(request, 'indice.html')
def musica(request):
    return render(request, 'musica.html')
def film(request):
    return render(request, 'film.html')

