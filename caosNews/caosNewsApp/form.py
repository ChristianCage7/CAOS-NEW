from django import forms
from .models import Noticia, Usuarios

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'fecha', 'imagen', 'categoria', 'id_usuario', 'ubicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'id_usuario': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        # Actualizar el queryset para el campo id_usuario
        self.fields['id_usuario'].queryset = Usuarios.objects.filter(estado=1)
