from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('crud/', views.crud, name='crud'),
    path('noticia-carrusel-1', views.noticia_carrusel_1, name='noticia_carrusel_1'),
    path('noticia-carrusel-2', views.noticia_carrusel_2, name='noticia_carrusel_2'),
    path('noticia-carrusel-3', views.noticia_carrusel_3, name='noticia_carrusel_3'),
    path('deportes/', views.cat_deportes, name='cat_deportes'),
    path('economia/', views.cat_economia, name='cat_economia'),
    path('internacional/', views.cat_internacional, name='cat_internacional'),
    path('politica/', views.cat_politica, name='cat_politica'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('planes/', views.planes, name='planes'),
    path('form_noticia/', views.form_noticia, name='form_noticia'),

]