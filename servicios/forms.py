from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EventoAgro, ServicioAgro


class RegistroUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username',)
        labels = {
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': 'Hasta 150 caracteres. Puede incluir letras, números y @/./+/-/_.',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Elegí un nombre de usuario',
                'autocomplete': 'username',
                'autofocus': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password1'].help_text = (
            'Usá al menos 8 caracteres y evitá contraseñas comunes o fáciles de adivinar.'
        )
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500',
            'placeholder': 'Creá una contraseña segura',
            'autocomplete': 'new-password',
        })
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['password2'].help_text = 'Ingresá la misma contraseña nuevamente para confirmarla.'
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500',
            'placeholder': 'Repetí tu contraseña',
            'autocomplete': 'new-password',
        })


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