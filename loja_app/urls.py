from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('info_produtos/<int:id>/', views.info_produtos, name='info_produtos'),
    path('categorias/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('busca/', views.buscaProduto, name='busca_produtos'),
    path('produtos_em_oferta/', views.produtoEmOfertas, name = 'produtos_em_oferta')
]

