from django.urls import path
from . import views

urlpatterns = [
    # Parte pública
    path('', views.lista_produtos, name='lista_produtos'),
    path('info_produtos/<int:id>/', views.info_produtos, name='info_produtos'),
    path('categorias/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('busca/', views.buscaProduto, name='busca_produtos'),
    path('produtos_em_oferta/', views.produtoEmOfertas, name='produtos_em_oferta'),

    # Autenticação admin
    path('accounts/login/', views.login_admin, name='login'),
    path('logout/', views.logout_admin, name='logout_admin'),

    # Área administrativa
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/produtos/cadastrar/', views.cadastrarProdutos, name='cadastrar_produtos'),
    path('dashboard/produtos/', views.listar_produtos, name='listar_produtos'),
    path('dashboard/produtos/editar/<int:produto_id>/', views.editar_produtos, name='editar_produtos'),
    path('dashboard/produtos/excluir/<int:produto_id>/', views.excluir_produtos, name='excluir_produto'),

    path('dashboard/categorias/', views.listar_categorias, name='listar_categorias'),
    path('dashboard/categorias/cadastrar/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('dashboard/categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('dashboard/categorias/excluir/<int:categoria_id>/', views.excluir_categoria, name='excluir_categoria'),
]
