# roteiros/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Roteiros
    path('', views.listar_roteiros, name='listar_roteiros'),
    path('criar_roteiro/', views.criar_roteiro, name='criar_roteiro'),
    path('roteiro/<int:roteiro_id>/', views.detalhes_roteiro, name='detalhes_roteiro'),
    path('roteiro/<int:roteiro_id>/editar/', views.editar_roteiro, name='editar_roteiro'),
    path('roteiro/<int:roteiro_id>/excluir/', views.excluir_roteiro, name='excluir_roteiro'),

    # Destinos
    path('roteiro/<int:roteiro_id>/destinos/', views.listar_destinos, name='listar_destinos'),
    path('roteiro/<int:roteiro_id>/criar_destino/', views.criar_destino, name='criar_destino'),
    path('roteiro/<int:roteiro_id>/editar_destino/<int:destino_id>/', views.editar_destino, name='editar_destino'),
    path('roteiro/<int:roteiro_id>/excluir_destino/<int:destino_id>/', views.excluir_destino, name='excluir_destino'),

    # Pontos Turísticos
    path('roteiro/<int:roteiro_id>/pontos_turisticos/', views.listar_pontos_turisticos, name='listar_pontos_turisticos'),
    path('roteiro/<int:roteiro_id>/criar_ponto_turistico/', views.criar_ponto_turistico, name='criar_ponto_turistico'),
    path('roteiro/<int:roteiro_id>/editar_ponto_turistico/<int:ponto_turistico_id>/', views.editar_ponto_turistico, name='editar_ponto_turistico'),
    path('roteiro/<int:roteiro_id>/excluir_ponto_turistico/<int:ponto_turistico_id>/', views.excluir_ponto_turistico, name='excluir_ponto_turistico'),

    # Restaurantes
    path('roteiro/<int:roteiro_id>/restaurantes/', views.listar_restaurantes, name='listar_restaurantes'),
    path('roteiro/<int:roteiro_id>/criar_restaurante/', views.criar_restaurante, name='criar_restaurante'),
    path('roteiro/<int:roteiro_id>/editar_restaurante/<int:restaurante_id>/', views.editar_restaurante, name='editar_restaurante'),
    path('roteiro/<int:roteiro_id>/excluir_restaurante/<int:restaurante_id>/', views.excluir_restaurante, name='excluir_restaurante'),

    # Atividades
    path('roteiro/<int:roteiro_id>/atividades/', views.listar_atividades, name='listar_atividades'),
    path('roteiro/<int:roteiro_id>/criar_atividade/', views.criar_atividade, name='criar_atividade'),
    path('roteiro/<int:roteiro_id>/editar_atividade/<int:atividade_id>/', views.editar_atividade, name='editar_atividade'),
    path('roteiro/<int:roteiro_id>/excluir_atividade/<int:atividade_id>/', views.excluir_atividade, name='excluir_atividade'),
]
