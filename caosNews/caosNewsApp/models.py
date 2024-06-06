from django.db import models

# Create your models here.

class Registrar(models.Model):
    id_usuario = models.AutoField(db_column='id_usuario', primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=20, blank=False, null=False)
    apellido = models.CharField(db_column='apellido', max_length=20, blank=False, null=False)
    email = models.EmailField(db_column='email', max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(db_column='password', max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)

class Noticia(models.Model):
    id_noticia = models.AutoField(db_column='id_noticia', primary_key=True)
    titulo = models.CharField(db_column='titulo', max_length=100, blank=False, null=False)
    cuerpo = models.CharField(db_column='cuerpo', max_length=500, blank=False, null=False)
    fecha = models.DateField(db_column='fecha',blank=False, null=False)  
    id_usuario = models.ForeignKey('Registrar',on_delete=models.CASCADE, db_column='id_usuario')
    ubicacion = models.CharField(db_column='ubicacion', max_length=50, blank=False, null=False)
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='categoria') 
    imagen = models.BooleanField(db_column='imagen',null=True)

    def __str__(self):
        return str(self.titulo)
    
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='id_categoria', primary_key=True)
    categoria = models.CharField(db_column='categoria', max_length=15, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)
