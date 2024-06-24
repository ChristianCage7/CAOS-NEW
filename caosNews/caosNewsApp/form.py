from django import forms
from django.contrib.auth.models import User
from .models import Noticia
from django.contrib.auth import get_user_model

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'fecha', 'imagen', 'categoria', 'usuario', 'ubicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].queryset = User.objects.all()
        self.fields['usuario'].label_from_instance = lambda obj: f"{obj.get_full_name()} ({obj.username})"