from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages  # Correção aqui

from .forms import ProdutoForm, CategoriaForm
from .models import Produto, Categoria
from django.db.models import Q


# Lista de produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produto': produtos})


# Detalhes do produto
def info_produtos(request, id):
    produtos = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/info_produtos.html', {'produto': produtos})


# Produtos por categoria
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


# Busca de produtos
def buscaProduto(request):
    termo = request.GET.get('q')  # Obtém o termo da busca
    produtos = Produto.objects.filter(
        Q(nome__icontains=termo) | Q(categoria__nome__icontains=termo)
    ) if termo else Produto.objects.none()  # Verifica se o termo foi fornecido

    return render(request, 'produtos/busca_produtos.html', {'produtos': produtos, 'termo': termo})


# Produtos em oferta
def produtoEmOfertas(request):
    contexto = {}
    try:
        produto_em_promocao = Categoria.objects.get(nome='Promoção')
        produto_em_promocao = Produto.objects.filter(categoria=produto_em_promocao)
        if produto_em_promocao.exists():
            contexto['produtos'] = produto_em_promocao
    except Categoria.DoesNotExist():
        contexto['erro'] = 'Nenhum produto adicionado no momento.'
    return render(request, 'produtos/produtos_em_oferta.html', contexto)


# Login de administrador
def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'areaAdmin/login.html')


# Verifica se o usuário é admin
def is_admin(user):
    return user.is_staff


# Área de administração
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'areaAdmin/admin_dashboard.html')


# Cadastrar produto
@login_required
@user_passes_test(is_admin)
def cadastrarProdutos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'areaAdmin/cadastrar_produtos.html', {'form': form})

def logout_admin(request):
    auth_logout(request)
    return redirect('login')

#listar os produtos no dashboard
@login_required
@user_passes_test(is_admin)
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'areaAdmin/listar_pordutos.html', {'produtos':produtos})


#editar os produtos
@login_required
@user_passes_test(is_admin)
def editar_produtos(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'areaAdmin/editar_produtos.html', {'form':form})


#excluir produtos
@login_required
@user_passes_test(is_admin)
def excluir_produtos(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect('listar_produtos')



# Listar categorias
@login_required
@user_passes_test(is_admin)
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'areaAdmin/listar_categorias.html', {'categorias': categorias})


# Cadastrar categoria
@login_required
@user_passes_test(is_admin)
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'areaAdmin/cadastrar_categoria.html', {'form': form})


# Editar categoria
@login_required
@user_passes_test(is_admin)
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'areaAdmin/editar_categoria.html', {'form': form})


# Excluir categoria
@login_required
@user_passes_test(is_admin)
def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    messages.success(request, 'Categoria excluída com sucesso!')
    return redirect('listar_categorias')