from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_produtos, name = 'lista_produtos'),
    path('info_produtos/<int:id>/',views.info_produtos, name = 'info_produtos'),

]