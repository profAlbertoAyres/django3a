from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'web/home.html')

def contato(request):
    return render(request, 'web/contato.html')
