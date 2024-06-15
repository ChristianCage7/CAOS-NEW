from django.contrib import admin
from .models import Usuarios, Noticia, Categoria
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Noticia)
admin.site.register(Categoria)