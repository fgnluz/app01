# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='inscricao',
            name='telefone',
        ),
    ]
