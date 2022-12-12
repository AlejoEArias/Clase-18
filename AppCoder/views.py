from django.shortcuts import render
from .models import familiar
from django.http import HttpResponse

# Create your views here.

def familiar (request):

    integrante_1 = familiar (nombre="Alejo", edad=26, fecha_nacimiento="12/12/1996")
    integrante_2 = familiar (nombre="Cristina", edad=60, fecha_nacimiento="07/12/1962")
    integrante_3 = familiar (nombre="Nico", edad=30, fecha_nacimiento="17/07/1992")

    integrante_1.save()
    integrante_2.save()
    integrante_3.save()

    return HttpResponse(integrante_1, integrante_2, integrante_3)