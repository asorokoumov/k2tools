# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SoleForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


# step 0
def create_order(request):
    return redirect('choose_sole')


# step 1
def choose_sole(request):
    return render(request, 'create_order/choose_sole.html')


# step 2
def choose_shape(request):
    if request.method == "POST":
        return render(request, 'create_order/choose_shape.html')
    else:
        return redirect('choose_sole')


# step 3
def choose_fabric(request):
    if request.method == "POST":
        return render(request, 'create_order/choose_fabric.html')
    else:
        return redirect('choose_sole')


# step 4
def choose_other(request):
    if request.method == "POST":
        return render(request, 'create_order/choose_other.html')
    else:
        return redirect('choose_sole')


# step 5
def choose_sizes(request):
    if request.method == "POST":
        return render(request, 'create_order/choose_sizes.html')
    else:
        return redirect('choose_sole')


# step 6
def enter_order_data(request):
    if request.method == "POST":
        return render(request, 'create_order/enter_order_data.html')
    else:
        return redirect('choose_sole')


# step 7
def confirm_order(request):
    if request.method == "POST":
        return render(request, 'create_order/confirm_order.html')
    else:
        return redirect('choose_sole')