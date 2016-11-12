# -*- coding: utf-8 -*-
from django import forms
from app01.models import Inscricao
from app01.models import Despesa

class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = '__all__'

class DespesaForm(forms.ModelForm):

    class Meta:
        model = Despesa
        fields = '__all__'