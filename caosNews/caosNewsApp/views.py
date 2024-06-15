from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'caosNewsApp/index.html')

def base(request):
    return render(request, 'caosNewsApp/base.html')

def crud(request): 
    return render(request, 'caosNewsApp/base.html')

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

#def alumnosAdd(request):
    rut=request.POST['rut']  #Se recuperan los datos del formulario y se asignan a variables locales
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    email=request.POST['email']
    password=request.POST['password']
    estado="1"

    obj=Usuarios.objects.create(rut=rut,
                                nombre=nombre,
                                apellido=apellido,
                                email=email,
                                password=password,
                                estado=1)
    obj.save()                                       #Se graba el objeto en la tabla y retorna al formulario.
    context={'mensaje':"Datos grabados"}
    return render(request, 'caosNewsApp/usuario_add.html', context)