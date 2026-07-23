from django import forms
from .models import EventoAgro, ServicioAgro


class EventoForm(forms.ModelForm):
    class Meta:
        model = EventoAgro
        fields = ['titulo', 'descripcion', 'fecha', 'ubicacion']
        # Usamos un widget especial para que el navegador dibuje un calendario con hora nativo
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'w-full px-4 py-2 border rounded-xl'}),
            'titulo': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-xl'}),
            'ubicacion': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-xl'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-xl', 'rows': 4}),
        }


class ServicioForm(forms.ModelForm):
    class Meta:
        model = ServicioAgro

        fields = ['tipo_oferta','titulo', 'categoria', 'descripcion', 'ubicacion', 'contacto']
        widgets = {
            'tipo_oferta': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-xl bg-gray-50'}),
            'titulo': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-xl', 'placeholder': 'Ej: Fumigación mosquito'}),
            'categoria': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-xl'}),
            'ubicacion': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-xl'}),
            'contacto': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-xl', 'placeholder': 'Ej: 5491123456789'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-xl', 'rows': 4, 'placeholder': 'Detallá tu experiencia, maquinaria, precio estimado, etc.'}),
        }