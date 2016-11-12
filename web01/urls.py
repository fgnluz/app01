# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from app01.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app01.views',
url(r'^$', 'home', name='home'),
url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
url(r'^lista/$', Lista.as_view(), name='lista'),
url(r'^admin/', include(admin.site.urls)),
url(r'^despesas/$', CriarDespesa.as_view(), name='despesas'),
url(r'^listadespesas/$', ListaDespesas.as_view(), name='listadespesas'),
)