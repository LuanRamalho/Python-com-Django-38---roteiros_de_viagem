from django import forms
from .models import Roteiro, Destino, PontoTuristico, Restaurante, Atividade

class RoteiroForm(forms.ModelForm):
    class Meta:
        model = Roteiro
        fields = ['nome', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y'),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y'),
        }

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['nome', 'descricao']

class PontoTuristicoForm(forms.ModelForm):
    class Meta:
        model = PontoTuristico
        fields = ['nome', 'descricao']

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nome', 'descricao', 'custo']

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['nome', 'descricao', 'data_atividade']
        widgets = {
            'data_atividade': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/YYYY'}, format='%d/%m/%Y'),
        }
