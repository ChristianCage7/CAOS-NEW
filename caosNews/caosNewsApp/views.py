from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .form import NoticiaForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'caosNewsApp/index.html')

def base(request):
    return render(request, 'caosNewsApp/base.html')

def crud_noticia(request):
    if request.user.is_staff:
        noticias = Noticia.objects.filter(estado=1)
        title = "Moderación de Noticias"
    else:
        noticias = Noticia.objects.filter(estado=1, usuario=request.user)
        title = "Tus Noticias"
    return render(request, 'caosNewsApp/crud_noticia.html', {'noticias': noticias, 'title': title})


def noticia_carrusel_1(request):
    return render(request, 'caosNewsApp/noticia_carrusel_1.html')

def noticia_carrusel_2(request):
    return render(request, 'caosNewsApp/noticia_carrusel_2.html')

def noticia_carrusel_3(request):
    return render(request, 'caosNewsApp/noticia_carrusel_3.html')

def cat_deportes(request):
    return render(request, 'caosNewsApp/cat_deportes.html')

def cat_economia(request):
    return render(request, 'caosNewsApp/cat_economia.html')

def cat_internacional(request):
    return render(request, 'caosNewsApp/cat_internacional.html')

def cat_politica(request):
    return render(request, 'caosNewsApp/cat_politica.html')

def quienes_somos(request):
    return render(request, 'caosNewsApp/quienes_somos.html')

def planes(request):
    return render(request, 'caosNewsApp/planes.html')

def form_noticia(request):
    return render(request, 'caosNewsApp/form_noticia.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'caosNewsApp/user_list.html', {'users': users})

def user_add(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario agregado exitosamente.")
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'caosNewsApp/user_add.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado exitosamente.")
            return redirect('user_list')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'caosNewsApp/user_edit.html', {'form': form, 'user': user})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, "Usuario eliminado con éxito.")
    return redirect('user_list') 

def noticias_add(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Noticia agregada exitosamente.")
            return redirect('crud_noticia')
    else:
        form = NoticiaForm()
    return render(request, 'caosNewsApp/noticias_add.html', {'form': form})

def noticias_edit(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        # Procesar el formulario
        return redirect('crud_noticia')
    return render(request, 'caosNewsApp/noticias_edit.html', {'noticia': noticia})

def noticias_eliminar(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, "Noticia eliminada con éxito.")
        return redirect('crud_noticia')
    return redirect('crud_noticia')

def revision_noticias(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'caosNewsApp/revision_noticias.html', {'noticia': noticia})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos')
    return render(request, 'base.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado exitosamente.")
            return redirect('user_list')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'caosNewsApp/user_edit.html', {'form': form, 'user': user})