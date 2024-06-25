from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    ESTADOS = (
        (0, 'Inactivo'),
        (1, 'Activo'),
        (2, 'Rechazada')  # Añadir el nuevo estado "Rechazada"
    )

    id_noticia = models.AutoField(db_column='id_noticia', primary_key=True)
    titulo = models.CharField(db_column='titulo', max_length=100)
    cuerpo = models.TextField(db_column='cuerpo', max_length=500)
    fecha = models.DateField(db_column='fecha')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="noticias")
    ubicacion = models.CharField(db_column='ubicacion', max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='categoria')
    imagen = models.ImageField(db_column='imagen', upload_to='noticias/', null=True, blank=True)
    estado = models.IntegerField(db_column='estado', choices=ESTADOS, default=0)
    
    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='id_categoria', primary_key=True)
    categoria = models.CharField(db_column='categoria', max_length=15)

    def __str__(self):
        return self.categoria
