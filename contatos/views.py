from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from contatos.models import *


# Create your views here.

def hello(request):
    query = Pessoa.objects.all()
    return render(request, "contatos/listar.html", {'pessoas': query})


def adicionar(request):
    if request.method == 'POST':
        params = request.POST
        nome = params.get("nome", None)
        idade = params.get("idade", None)
        url = params.get("url", None)

        p = Pessoa()
        p.nome = nome
        p.idade = idade
        p.site = url
        p.datacadastro = '1111-11-11'

        p.save()

        return HttpResponseRedirect('/')
    else:
        return render(request, "contatos/novo.html")

def mostrar(request, id):

    if request.method == 'GET':
        query = Pessoa.objects.filter(id=id)


        return render(request, "contatos/mostrar.html", {'pessoas': query})

def apagar(request, id):

    if request.method == 'GET':
        Pessoa.objects.filter(id=id).delete()

        return HttpResponseRedirect('/')

def editar (request, id):
    if request.method == 'POST':
        params = request.POST
        query = Pessoa.objects.get(pk=id)
        nome = params.get("nome", None)
        idade = params.get("idade", None)
        url = params.get("url", None)

        query.nome = nome
        query.idade = idade
        query.site = url
        query.datacadastro = '1111-11-11'

        query.save()

        return HttpResponseRedirect('/')
    return render(request, 'contatos/editar.html', {})






