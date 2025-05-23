# Generated by Django 5.1.7 on 2025-04-01 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField(default=0)),
                ('tamanhos', models.CharField(help_text='Exemplo: 37, 38, 39, 40', max_length=255)),
                ('foto_1', models.ImageField(blank=True, null=True, upload_to='media/produtos/')),
                ('foto_2', models.ImageField(blank=True, null=True, upload_to='media/produtos/')),
                ('foto_3', models.ImageField(blank=True, null=True, upload_to='media/produtos/')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('categoria_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='loja_app.categoria')),
            ],
        ),
    ]
