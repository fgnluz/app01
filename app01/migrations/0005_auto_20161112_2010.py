# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20161111_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('despesa', models.CharField(max_length=300)),
                ('valor', models.DecimalField(max_digits=5, decimal_places=2)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'despesa',
                'ordering': ['criado_em'],
                'verbose_name_plural': 'despesas',
            },
        ),
        migrations.DeleteModel(
            name='AtividadeC',
        ),
    ]
