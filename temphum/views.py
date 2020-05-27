from django.shortcuts import render, HttpResponse
import requests

# Create your views here.


def temphum(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        latitud = request.GET['latitud']
        mes = request.GET['mes']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value, 'latitud': latitud, 'mes': mes}
            # response = requests.post('http://127.0.0.1:8000/temphums/', args)
            response = requests.post('http://pi1-eafit-jppenaf.azurewebsites.net/temphums/', args)
            # Convierte la respuesta en JSON
            temphum_json = response.json()

    # Realiza una petición GET al Web Services
    # response = requests.get('http://127.0.0.1:8000/temphums/')
    response = requests.get('http://pi1-eafit-jppenaf.azurewebsites.net/temphums/')
    # Convierte la respuesta en JSON
    temphums = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temphum/temphum.html", {'temphums': temphums})