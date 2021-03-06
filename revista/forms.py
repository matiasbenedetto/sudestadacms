#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django import forms

class ContactoForm (forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo Electrónico'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Telefono'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))