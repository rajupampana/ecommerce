# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):

    context = {'input': 'pottama'}
    template_name = 'base.html'
    return render(request, template_name, context)