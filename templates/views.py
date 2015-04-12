from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context
# Create your views here.


def processLogin(request):

    loggin = ""
    if request.user.is_authenticated():
        loggin += "Logged in as " + request.user.username + ". "
        loggin += "<a href='/admin/logout/'>Logout</a><br>"
    else:
        loggin += "Not logged in. "
        loggin += "<a href='/admin/login/'>Login</a><br>"
    return loggin


def processCMS_Users(request, recurso):

    loggin = processLogin(request)

    if request.method == "GET":
        try:
            fila = Page.objects.get(name=recurso)
            print fila.page
            return HttpResponse(loggin + "<br>" + fila.page)
        except Page.DoesNotExist:
            return HttpResponseNotFound(loggin +
                                        "<br>Page not found: /%s" % recurso)
    elif request.method == "PUT":
        if request.user.is_authenticated():
            try:
                cuerpo = request.body
                fila = Page.objects.create(name=recurso, page=cuerpo)
                fila.save()
                return HttpResponse("Nueva fila")
            except:
                return HttpResponseNotFound("Error")
        else:
            return HttpResponseNotFound("No puedes modificarlo" +
                                        " si no estas auntetificado")


def processCMS_Templates(request, recurso):
    salida = ""
    loggin = processLogin(request)

    if request.method == "GET":
        try:
            fila = Page.objects.get(name=recurso)
            salida += fila.page
            plantilla = get_template('index.html')
            c = Context({'title': loggin, 'contenido': salida})
            renderizado = plantilla.render(c)
            return HttpResponse(renderizado)
        except Page.DoesNotExist:
            return HttpResponseNotFound(salida +
                                        "<br>Page not found: /%s" % recurso)


def show_all(request):
    salida = ""
    loggin = processLogin(request)
    groups = Page.objects.all()
    for fila in groups:
        salida += fila.name + " "
        salida += fila.page + "<br>"
    plantilla = get_template('index.html')
    c = Context({'title': loggin, 'contenido': salida})
    renderizado = plantilla.render(c)
    return HttpResponse(renderizado)
