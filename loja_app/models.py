from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    categoria_pai = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='subcategorias',
    )

    def __str__(self):
        return self.nome



class Produto(models.Model):
    objects = None
    nome = models.CharField(max_length=255)
    preco_dinheiro = models.DecimalField(max_digits=10, decimal_places=2)
    preco_cartao = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    tamanhos = models.CharField(max_length=255, help_text="Exemplo: 37, 38, 39, 40")
    foto_1 = models.ImageField(upload_to='media/produtos/', blank=True, null=True)
    foto_2 = models.ImageField(upload_to='media/produtos/', blank=True, null=True)
    foto_3 = models.ImageField(upload_to='media/produtos/', blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nome} - R$ {self.preco_dinheiro:.2f} (Dinheiro) / R$ {self.preco_cartao:.2f} (Cartão)"

    def clean(self):
        if self.preco_dinheiro < 0:
            raise ValidationError("O preço em dinheiro não pode ser negativo.")
        if self.preco_cartao < 0:
            raise ValidationError("O preço no cartão não pode ser negativo.")
        if self.quantidade_estoque < 0:
            raise ValidationError("A quantidade de estoque não pode ser menor que zero.")





@receiver(post_delete, sender=Produto)
def delete_associated_file(sender, instance, **kwargs):
    # Verifica cada campo de imagem e remove o arquivo, se existir
    for image_field in ['foto_1', 'foto_2', 'foto_3']:
        image = getattr(instance, image_field)
        if image and image.path:  # Confirma que o arquivo existe
            try:
                os.remove(image.path)  # Remove o arquivo do sistema de arquivos
            except FileNotFoundError:
                pass