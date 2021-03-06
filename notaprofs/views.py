from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from profs.models import *
from django.http import HttpResponseRedirect, HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from django import forms

"""class ProdutoForm(forms.Form):
	nome = forms.CharField(max_length=100)
	preco = forms.IntegerField()
	descricao = forms.CharField(max_length=255)
	urlFoto = forms.CharField(max_length=255)
"""
def home(request):
	return render(request, 'index.html')

def perfil(request):
	code = request.POST.get('code')
	professor = Professor.objects.get(id = code)
	context = {'professor':professor}
	return render(request, 'perfil.html', context)

def top(request):
	professor = Professor.objects.order_by('-media')[0:10]
	context = {'professor':professor}
	return render(request, 'top.html',context)

def todos(request):
	professor = Professor.objects.all()
	context = {'professor':professor}
	return render(request, 'todos.html',context)

def search(request):
	name = request.POST.get('prof')
	professor = Professor.objects.filter(nome__icontains = name)
	if ( professor.count()==1):
		context = {'code':professor[0].id}
		return render(request, 'redirect.html',context)
	elif (professor.count()==0):
		return render(request, 'lista.html')
	else:
		context = {'professor':professor}
		return render(request, 'lista.html',context) 
def oque(request):
	return render(request, 'oque.html')

def votar(request):
	code = request.POST.get('code')
	context = {'code':code}
	return render(request, 'votar.html',context)

def voto(request):
	code = request.POST.get('code')
	uid = request.POST.get('uid')
	voto1 = int(request.POST.get('Cat1'))
	voto2 = int(request.POST.get('Cat2'))
	voto3 = int(request.POST.get('Cat3'))
	if voto1>10:
		voto1=10
	elif voto1<0:
		voto1=0
	if voto2>10:
		voto2=10
	elif voto2<0:
		voto2=0
	if voto3>10:
		voto3=10
	elif voto3<0:
		voto3=0
	professor = Professor.objects.get(id=code)
	professor.notaCat1=(professor.notaCat1*professor.numVotos+voto1)/(professor.numVotos+1)
	professor.notaCat2=(professor.notaCat2*professor.numVotos+voto2)/(professor.numVotos+1)
	professor.notaCat3=(professor.notaCat3*professor.numVotos+voto3)/(professor.numVotos+1)
	professor.numVotos=professor.numVotos+1
	professor.media=(professor.notaCat1+professor.notaCat2+professor.notaCat3)/3
	professor.alunos = professor.alunos + "," + uid;
	professor.save()
	context = {'code':code}
	return render(request, 'redirect.html', context)
