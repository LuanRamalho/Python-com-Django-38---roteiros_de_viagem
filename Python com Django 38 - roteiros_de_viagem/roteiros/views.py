from django.shortcuts import render, redirect, get_object_or_404
from .models import Roteiro, Destino, PontoTuristico, Restaurante, Atividade
from .forms import RoteiroForm, DestinoForm, PontoTuristicoForm, RestauranteForm, AtividadeForm

# Roteiro Views
def criar_roteiro(request):
    if request.method == 'POST':
        form = RoteiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_roteiros')
    else:
        form = RoteiroForm()
    return render(request, 'roteiros/criar_roteiro.html', {'form': form})

def listar_roteiros(request):
    roteiros = Roteiro.objects.all()
    return render(request, 'roteiros/listar_roteiros.html', {'roteiros': roteiros})

def editar_roteiro(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    if request.method == 'POST':
        form = RoteiroForm(request.POST, instance=roteiro)
        if form.is_valid():
            form.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    else:
        form = RoteiroForm(instance=roteiro)
    return render(request, 'roteiros/editar_roteiro.html', {'form': form})

def excluir_roteiro(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    if request.method == 'POST':
        roteiro.delete()
        return redirect('listar_roteiros')
    return render(request, 'roteiros/excluir_roteiro.html', {'roteiro': roteiro})

def detalhes_roteiro(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    
    # Buscar todos os destinos, atividades, pontos turísticos e restaurantes associados ao roteiro
    destinos = roteiro.destinos.all()
    atividades = roteiro.atividades.all()  # AQUI você precisa garantir que está pegando as atividades
    pontos_turisticos = roteiro.pontos_turisticos.all()
    restaurantes = roteiro.restaurantes.all()

    return render(request, 'roteiros/detalhes_roteiro.html', {
        'roteiro': roteiro,
        'destinos': destinos,
        'atividades': atividades,  # Passe as atividades para o template
        'pontos_turisticos': pontos_turisticos,
        'restaurantes': restaurantes,
    })

# Destino Views
def criar_destino(request, roteiro_id):
    roteiro = Roteiro.objects.get(id=roteiro_id)
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            destino = form.save(commit=False)
            destino.roteiro = roteiro
            destino.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    else:
        form = DestinoForm()
    return render(request, 'roteiros/criar_destino.html', {'form': form})

def listar_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'listar_destinos.html', {'destinos': destinos})

def editar_destino(request, roteiro_id, destino_id):
    destino = get_object_or_404(Destino, id=destino_id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro_id)
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'roteiros/editar_destino.html', {'form': form})


def excluir_destino(request, roteiro_id, destino_id):
    destino = get_object_or_404(Destino, id=destino_id)
    roteiro = destino.roteiro  # Pegando o roteiro associado ao destino
    if request.method == 'POST':
        destino.delete()
        return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    return render(request, 'roteiros/excluir_destino.html', {'destino': destino, 'roteiro': roteiro})

# Criar um novo ponto turístico dentro de um roteiro
def criar_ponto_turistico(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)  # Busca o roteiro correto
    if request.method == 'POST':
        form = PontoTuristicoForm(request.POST)
        if form.is_valid():
            ponto = form.save(commit=False)
            ponto.roteiro = roteiro  # Agora o ponto pertence ao roteiro, não ao destino
            ponto.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    else:
        form = PontoTuristicoForm()
    
    return render(request, 'roteiros/criar_ponto_turistico.html', {'form': form, 'roteiro': roteiro})

# Listar pontos turísticos de um roteiro específico
def listar_pontos_turisticos(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    pontos_turisticos = roteiro.pontoturistico_set.all()  # Busca pontos turísticos do roteiro
    return render(request, 'roteiros/listar_pontos_turisticos.html', {'pontos_turisticos': pontos_turisticos, 'roteiro': roteiro})

# Editar um ponto turístico dentro de um roteiro
def editar_ponto_turistico(request, roteiro_id, ponto_turistico_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    ponto = get_object_or_404(PontoTuristico, id=ponto_turistico_id, roteiro=roteiro)
    
    if request.method == 'POST':
        form = PontoTuristicoForm(request.POST, instance=ponto)
        if form.is_valid():
            form.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    else:
        form = PontoTuristicoForm(instance=ponto)
    
    return render(request, 'roteiros/editar_ponto_turistico.html', {'form': form, 'roteiro': roteiro})

# Excluir um ponto turístico dentro de um roteiro
def excluir_ponto_turistico(request, roteiro_id, ponto_turistico_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    ponto = get_object_or_404(PontoTuristico, id=ponto_turistico_id, roteiro=roteiro)
    
    if request.method == 'POST':
        ponto.delete()
        return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    
    return render(request, 'roteiros/excluir_ponto_turistico.html', {'ponto': ponto, 'roteiro': roteiro})

# Criar um novo restaurante dentro de um roteiro
def criar_restaurante(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)  # Buscar o roteiro correto

    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            restaurante = form.save(commit=False)
            restaurante.roteiro = roteiro  # Associando o restaurante ao roteiro
            restaurante.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    else:
        form = RestauranteForm()

    return render(request, 'roteiros/criar_restaurante.html', {'form': form, 'roteiro': roteiro})

# Listar restaurantes de um roteiro específico
def listar_restaurantes(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    restaurantes = roteiro.restaurante_set.all()  # Obtendo restaurantes do roteiro

    return render(request, 'roteiros/listar_restaurantes.html', {'restaurantes': restaurantes, 'roteiro': roteiro})

# Editar um restaurante dentro de um roteiro
def editar_restaurante(request, roteiro_id, restaurante_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    restaurante = get_object_or_404(Restaurante, id=restaurante_id, roteiro=roteiro)

    if request.method == 'POST':
        form = RestauranteForm(request.POST, instance=restaurante)
        if form.is_valid():
            form.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)
    else:
        form = RestauranteForm(instance=restaurante)

    return render(request, 'roteiros/editar_restaurante.html', {'form': form, 'roteiro': roteiro})

# Excluir um restaurante dentro de um roteiro
def excluir_restaurante(request, roteiro_id, restaurante_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    restaurante = get_object_or_404(Restaurante, id=restaurante_id, roteiro=roteiro)

    if request.method == 'POST':
        restaurante.delete()
        return redirect('detalhes_roteiro', roteiro_id=roteiro.id)

    return render(request, 'roteiros/excluir_restaurante.html', {'restaurante': restaurante, 'roteiro': roteiro})

# Atividade Views
def criar_atividade(request, roteiro_id):
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)
    
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.roteiro = roteiro  # Associar a atividade ao roteiro
            atividade.save()
            return redirect('detalhes_roteiro', roteiro_id=roteiro.id)  # Redireciona para a página de detalhes do roteiro
    else:
        form = AtividadeForm()

    return render(request, 'roteiros/criar_atividade.html', {'form': form, 'roteiro': roteiro})

def listar_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'listar_atividades.html', {'atividades': atividades})

def editar_atividade(request, roteiro_id, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('detalhes_destino', destino_id=atividade.destino.id)
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'roteiros/editar_atividade.html', {'form': form})

def excluir_atividade(request, roteiro_id, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id, roteiro_id=roteiro_id)
    roteiro = get_object_or_404(Roteiro, id=roteiro_id)  # Certifica que roteiro existe

    if request.method == 'POST':
        atividade.delete()
        return redirect('detalhes_roteiro', roteiro_id=roteiro_id)

    return render(request, 'roteiros/excluir_atividade.html', {
        'atividade': atividade,
        'roteiro': roteiro,  # Adicionando ao contexto
    })
