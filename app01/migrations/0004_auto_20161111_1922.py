# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20161111_1918'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Atividade',
            new_name='AtividadeC',
        ),
    ]
