# -*- coding: utf-8 -*-
from django import forms
from app01.models import Inscricao

class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = '__all__'
