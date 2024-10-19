from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meus-materiais/', views.index, name='meus_materiais'),
    path('configuracoes/', views.index, name='configuracoes'),
    path('area-do-usuario/', views.index, name='area_do_usuario'),
    path('sobre-nos/', views.index, name='sobre_nos'),
]
