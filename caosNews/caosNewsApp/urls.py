from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
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
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('noticias_add/', views.noticias_add, name='noticias_add'),
    path('noticias_editar/<int:pk>/', views.noticias_edit, name='noticias_edit'),
    path('noticias_eliminar/<int:pk>/', views.noticias_eliminar, name='noticias_eliminar'),
    path('revision_noticias/<int:pk>/', views.revision_noticias, name='revision_noticias'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)