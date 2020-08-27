from django.shortcuts import render, HttpResponse
from subprocess import run, PIPE
import requests, sys

# Create your views here.

def excecute(request):

    return render(request, "Page/project01.html")

def external(request):

    out = run([sys.executable, 'C:\\Users\\andon\\OneDrive\\Documentos\\Cood\\pycood\\Hydrogen_Orbital.py'], shell=False, stdout=PIPE)
    print(out)

    return render(request, "Page/project01.html")

def home(request):
    
    return render(request, "Page/home.html")


def project01(request):

    return render(request, "Page/project01.html")


def project02(request):

    return render(request, "Page/project02.html")


def contact(request):

    return render(request, "Page/contact.html")

