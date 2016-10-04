from django.shortcuts import render
from django.http import HttpResponseRedirect
from contatos.models import *
from django.utils.timezone import datetime
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from contatos.serializers import *

# Create your views here.
class PessoaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pessoa.objects.all().order_by('datacadastro')
    serializer_class = UserSerializer


def principal(request):
    contact_list = Pessoa.objects.all()

    paginator = Paginator(contact_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, "contatos/listar.html", {'contacts': contacts})


def adicionar(request):
    form = PessoaForm(request.POST or None)
    form_cel = CelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid() and form_cel.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            url = form.cleaned_data['site']
            cel = form_cel.cleaned_data['numero']
            sexo = form.cleaned_data['sexo']
            tiponum = form_cel.cleaned_data['tiponum']

            p = Pessoa()
            p.nome = nome
            p.idade = idade
            p.site = url
            p.datacadastro = datetime.today()
            p.sexo = sexo
            p.save()

            if cel:
                d = Numero()
                d.pessoa = p
                d.numero = cel
                d.tiponum = tiponum
                d.save()

            messages.add_message(request, messages.INFO, 'Contato Adicionado')
            return HttpResponseRedirect('/')

    return render(request, "contatos/novo.html", {'form': form,'form_cel':form_cel})


def novonum(request, id):
    form_cel = CelForm(request.POST or None)

    if request.method == 'POST':
        if form_cel.is_valid():
            messages.add_message(request, messages.INFO, 'Numero Adicionado')
            cel = form_cel.cleaned_data['numero']
            tiponum = form_cel.cleaned_data['tiponum']
            query = Pessoa.objects.get(pk=id)
            numero = Numero()
            numero.pessoa = query
            numero.numero = cel
            numero.tiponum = tiponum

            numero.save()

            return render(request, "contatos/mostrar.html", {'pessoa': query})

    return render(request, "contatos/novonum.html", {'form_cel': form_cel})


def mostrar(request, id):
    query = Pessoa.objects.get(pk=id)
    return render(request, "contatos/mostrar.html", {'pessoa': query})


def apagar(request, id):
    query = Pessoa.objects.get(pk=id)
    nome = query.nome
    Pessoa.objects.filter(id=id).delete()
    Numero.objects.filter(pessoa = id).delete()

    messages.add_message(request, messages.INFO, 'Contato apagado: %s' % nome)
    return HttpResponseRedirect('/')


def editar(request, id):
    query = Pessoa.objects.get(pk=id)
    form = PessoaForm(request.POST or None, initial={'nome': query.nome, "idade": query.idade, "site": query.site})

    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            url = form.cleaned_data['site']
            sexo = form.cleaned_data['sexo']

            query.nome = nome
            query.idade = idade
            query.site = url
            query.datacadastro = datetime.today()
            query.sexo = sexo
            query.save()

            messages.add_message(request, messages.INFO, 'Edicao bem sucedida')
            return render(request, "contatos/mostrar.html", {'pessoa': query})

    return render(request, 'contatos/editar.html', {'form': form})

def addcsv (request):
    form = AddCSV(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            arquivo = request.FILES['csv']
            pessoas = []

            for line in arquivo:
                line = line.split(',')
                p = Pessoa()
                p.nome = line[0]
                p.idade = line[1]
                p.site = line[2]
                p.datacadastro = datetime.today()
                pessoas.append(p)

            Pessoa.objects.bulk_create(pessoas)

            messages.add_message(request, messages.INFO, 'Foram adicionados %s contatos' % len(pessoas))
            return HttpResponseRedirect('/')

    return render(request, "contatos/addcsv.html", {'form': form})









