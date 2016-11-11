# -*- coding: utf-8 -*-
from django.db import models

class Inscricao(models.Model):
        nome = models.CharField(max_length=100)
        idade = models.IntegerField()
        email = models.EmailField(unique=True)
        criado_em = models.DateTimeField('criado em', auto_now_add=True)

        class Meta:
                ordering = ['nome']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome
