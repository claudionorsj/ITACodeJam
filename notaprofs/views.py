from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
#from notaprofs.models import *
from django.http import HttpResponseRedirect, HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from django import forms

"""class ProdutoForm(forms.Form):
	nome = forms.CharField(max_length=100)
	preco = forms.IntegerField()
	descricao = forms.CharField(max_length=255)
	urlFoto = forms.CharField(max_length=255)
"""
#@csrf_exempt
def home(request):
	return render(request, 'index.html')

#@csrf_exempt
#def postar(request):
#	#produtoLista = Produto.objects.filter(id = 1)
#	#produto = produtoLista[0]
#	#context = {'produto':produto}
#	return render(request, 'commerce/postar.html')
#
#@csrf_exempt
#def login(request):
#	code = request.GET.get('code')
#	context = {'code' : code}
#	return render(request, 'commerce/login.html', context)
#@csrf_exempt	
#def friendlist (request):
#	access_token = request.GET.get('access_token')
#	context = {'access_token' : access_token}
#	return render(request, 'commerce/friendlist.html', context)
#	
#@csrf_exempt
#def adicionar(request):
#	produtoForm = ProdutoForm(request.POST)
#	nome = produtoForm.data['nome']
#	preco = produtoForm.data['preco']
#	descricao = produtoForm.data['descricao']
#	urlFoto = produtoForm.data['urlFoto']
#	produtoAdd = Produto(nome=nome,preco=preco,descricao=descricao,usuario=1,urlFoto=urlFoto)
#	produtoAdd.save()
#	return HttpResponseRedirect('/home')
#
