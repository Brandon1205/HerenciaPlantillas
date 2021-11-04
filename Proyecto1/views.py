from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre,apellido):

        self.nombre=nombre
        self.apellido=apellido



def Saludo(request): #primera vista

    p1=Persona("Profesor Juan", "Díaz")

   # nombre="Juan"
    #apellido="Díaz"
    temas=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    fecha_actual=datetime.datetime.now()

    #doc_externo=open("C:/Users/brand/Documents/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template('miplantilla.html')
    #ctx=Context({"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha":fecha_actual, "temas":temas})
    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha":fecha_actual, "temas":temas})


    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido":p1.apellido, "fecha":fecha_actual, "temas":temas})


def cursoC(request):

    fecha_actual=datetime.datetime.now()
    return render(request, "cursoC.html", {"fecha":fecha_actual})


def Despedida(request):

    return HttpResponse("Hasta luego mundo")

def fecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)
    
def calculaEdad(request,edad, anio):
    #edadActual=18
    periodo=anio-2021
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(anio, edadFutura)

    return HttpResponse(documento)
