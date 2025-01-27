# Farmacia/forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombre', 'teléfono', 'rol', 'nombre_usuario', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }