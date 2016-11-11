# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20161111_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('atividade', models.CharField(max_length=200)),
                ('criado_em', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
            ],
            options={
                'ordering': ['criado_em'],
            },
        ),
        migrations.AlterModelOptions(
            name='inscricao',
            options={'verbose_name': 'nome', 'ordering': ['nome'], 'verbose_name_plural': 'nomes'},
        ),
    ]
