from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria



def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produto':produtos})


def info_produtos(request,id):
    produtos = get_object_or_404(Produto,id=id)
    return render(request, 'produtos/info_produtos.html', {'produto':produtos})