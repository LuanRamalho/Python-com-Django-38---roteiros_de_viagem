from django.contrib import admin
from django.urls import path, include  # Importando o include para incluir as URLs da app roteiros

urlpatterns = [
    path('admin/', admin.site.urls),  # URL do painel de administração
    path('roteiros/', include('roteiros.urls')),  # Incluir as URLs da app roteiros

]
