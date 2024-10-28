# Generated by Django 5.1.1 on 2024-10-28 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_estilo', models.CharField(max_length=3)),
                ('estilo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pais', models.CharField(max_length=2)),
                ('pais', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('fechaIni', models.DateField()),
                ('fechaFin', models.DateTimeField()),
                ('estilos', models.ManyToManyField(to='appJukeBox.estilo')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appJukeBox.pais')),
            ],
        ),
    ]
