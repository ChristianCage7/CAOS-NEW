from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('crud_usuario/', views.crud_usuario, name='crud_usuario'),
    path('crud_noticia/', views.crud_noticia, name='crud_noticia'),
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
    path('usuarios_add/', views.usuarios_add, name='usuarios_add'),
    path('usuarios_eliminar/<int:id_usuario>/', views.usuarios_eliminar, name='usuarios_eliminar'),
    path('usuarios_edit/<int:pk>/', views.usuarios_edit, name='usuarios_edit'),
    path('noticias_add/', views.noticias_add, name='noticias_add'),
    path('noticias_editar/<int:pk>/', views.noticias_edit, name='noticias_edit'),
    path('noticias_eliminar/<int:pk>/', views.noticias_eliminar, name='noticias_eliminar')
]