from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'preco_dinheiro':forms.NumberInput(attrs={'class':'form-control'}),
            'preco_cartao': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'tamanhos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exemplo: 37, 38, 39'}),
            'foto_1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da categoria',
            }),
            'categoria_pai': forms.Select(attrs={
                'class': 'form-control',
            }),
        }