from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .form import NoticiaForm
from .models import *
# Create your views here.

def index(request):
    return render(request, 'caosNewsApp/index.html')

def base(request):
    return render(request, 'caosNewsApp/base.html')

def crud_usuario(request):
    usuarios = Usuarios.objects.filter(estado=1)  # Mostrar solo usuarios activos
    print("Usuarios cargados:", usuarios)  # Debug para ver qué datos se están cargando
    return render(request, 'caosNewsApp/crud_usuario.html', {'usuarios': usuarios})

def crud_noticia(request):
    noticias = Noticia.objects.filter(estado=1) 
    return render(request, 'caosNewsApp/crud_noticia.html', {'noticias': noticias})


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

def usuarios_add(request):
    if request.method != "POST":
        return render(request, 'caosNewsApp/usuarios_add.html')
    else:
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        email=request.POST["email"]
        password=request.POST["password"]
        estado="1"
        
        newUsuario= Usuarios.objects.create(nombre=nombre,
                                            apellido=apellido,
                                            email=email,
                                            password=password,
                                            estado=1)
        newUsuario.save()
        messages.success(request, "Usuario agregado exitosamente.")
        return redirect('crud_usuario')


def usuarios_eliminar(request, id_usuario):
    if request.method == 'POST':
        usuario = get_object_or_404(Usuarios, pk=id_usuario)
        usuario.estado = 0  # Cambiar el estado a inactivo
        usuario.save()  # Guardar el cambio en la base de datos
        messages.success(request, "Usuario desactivado exitosamente.")
        return redirect('crud_usuario')
    else:
        messages.error(request, "Método no permitido.")
        return redirect('crud_usuario')

def usuarios_edit(request, pk):
    # Obtener el usuario por ID o mostrar un error 404 si no existe
    usuario = get_object_or_404(Usuarios, pk=pk, estado=1)  # Asegura que el usuario esté activo

    if request.method == "POST":
        # Recuperar la información desde el formulario
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        password = request.POST.get("password")  # Considera manejar la contraseña de manera segura

        # Actualizar los datos del usuario
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.email = email
        if password:  # Actualiza la contraseña solo si se proporciona una nueva
            usuario.password = password
        
        usuario.save()  # Guardar los cambios en la base de datos
        messages.success(request, "Usuario actualizado exitosamente.")
        return redirect('crud_usuario')
    else:
        # Renderizar la página con los datos actuales del usuario para editarlos
        context = {
            'usuario': usuario
        }
        return render(request, 'caosNewsApp/usuarios_edit.html', context)

def noticias_add(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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