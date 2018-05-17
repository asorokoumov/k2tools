# -*- coding: utf-8 -*-

from django import forms
from django.forms import Textarea
from django.forms.widgets import Input, Select

from .models import OrderItem


class SoleForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('sole',)
        widgets = {
            'sole': Select(attrs={'class': 'dropdown', 'placeholder': 'Подошва'}),
        }