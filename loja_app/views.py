from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria
from django.db.models import Q


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produto':produtos})


def info_produtos(request,id):
    produtos = get_object_or_404(Produto,id=id)
    return render(request, 'produtos/info_produtos.html', {'produto':produtos})

def produtos_por_categoria(request):
    categorias = Categoria.objects.all()
    contexto = {}

    for categoria in categorias:
        produtos = Produto.objects.filter(categoria=categoria)
        if produtos.exists():
            contexto[categoria] = produtos

    return render(request, 'produtos/produtos_por_categorias.html', {
        'categorias_com_produtos': contexto
    })




def buscaProduto(request):
    termo = request.GET.get('q')  # Obtém o termo da busca
    produtos = Produto.objects.filter(
        Q(nome__icontains=termo) | Q(categoria__nome__icontains=termo)
    ) if termo else Produto.objects.none()  # Verifica se o termo foi fornecido

    return render(request, 'produtos/busca_produtos.html', {'produtos': produtos, 'termo': termo})