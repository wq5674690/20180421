#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)