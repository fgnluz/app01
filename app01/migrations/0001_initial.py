# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF', unique=True)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=20, blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name_plural': 'nomes',
                'verbose_name': 'nome',
                'ordering': ['criado_em'],
            },
        ),
    ]
