# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from app01.models import Inscricao
from app01.models import Despesa
from app01.forms import InscricaoForm
from app01.forms import DespesaForm

def home(request):
        return render(request,'index.html')

class Criar(CreateView):
        template_name = 'cadastro.html'
        model = Inscricao
        success_url = reverse_lazy('lista')
        form_class = InscricaoForm

class Lista(ListView):
        template_name = 'lista.html'
        model = Inscricao
        context_object = 'nome'

class CriarDespesa(CreateView):
        template_name = 'despesa.html'
        model = Despesa
        success_url = reverse_lazy('listadespesas')
        form_class = DespesaForm

class ListaDespesas(ListView):
        template_name = 'listadespesas.html'
        model = Despesa
