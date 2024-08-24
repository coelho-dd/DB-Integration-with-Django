from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def lista_dados(request):
    dados = Pessoa.objects.all() 
    return render(request, 'minha_tabela/lista_dados.html', {'dados': dados})