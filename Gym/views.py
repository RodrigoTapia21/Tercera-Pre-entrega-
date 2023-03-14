from django.shortcuts import render
from Gym.models import Bebida, Entrenador, Clase
from Gym.forms import BebidaForm, EntrenadorForm, ClaseForm

def index(request):
    return render(request, "Gym/padre.html")

#---------------FUNCION AGREGAR BEBIDA---------------#
def agregar_bebida(request):
    if request.method == 'POST':
        form = BebidaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            bebida = Bebida(
                nombre_bebida=data.get('nombre_bebida'),
                precio_bebida=data.get('precio_bebida'),
                marca_bebida= data.get('marca_bebida'),
                litros_bebida= data.get('litros_bebida'),
            )
            bebida.save()
            return render(request, 'Gym/bebida.html', )
        else:
            return render(request, 'Gym/bebida.html', {'form': form})
    form_bebida = BebidaForm()
    return render(request, 'Gym/bebida.html', {'form': form_bebida})
#---------------FUNCION BUSCAR BEBIDA---------------#
def buscar_bebida(request):
    if request.GET["nombre_bebida"]: 
        opcion=request.GET.get('nombre_bebida')
        context= {"bebidas":Bebida.objects.filter(nombre_bebida__icontains=opcion).all()} 
    return render(request, 'Gym/bebida.html', context)


#---------------FUNCION AGREGAR ENTRENADOR---------------#
def agregar_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            entrenador =Entrenador(
                nombre_entrenador=data.get('nombre_entrenador'),
                clase_entrenador=data.get('clase_entrenador'),
            )
            entrenador.save()
            return render(request, 'Gym/entrenador.html', )
        else:
            return render(request, 'Gym/entrenador.html', {'form': form})
    form_entrenador = EntrenadorForm()
    return render(request, 'Gym/entrenador.html', {'form': form_entrenador})
#---------------FUNCION BUSCAR CLASE---------------#
def buscar_entrenador(request):
    if request.GET["nombre_entrenador"]: 
        opcion=request.GET.get('nombre_entrenador')
        context= {"entrenadores":Entrenador.objects.filter(nombre_entrenador__icontains=opcion).all()} 
    return render(request, 'Gym/entrenador.html', context)


#---------------FUNCION AGREGAR CLASE---------------#
def agregar_clase(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            clase = Clase(
                nombre_clase=data.get('nombre_clase'),
                precio_clase= data.get('precio_clase'),
            )
            clase.save()
            return render(request, 'Gym/clase.html', )
        else:
            return render(request, 'Gym/clase.html', {'form': form})
    form_clase = ClaseForm()
    return render(request, 'Gym/clase.html', {'form': form_clase})
#---------------FUNCION BUSCAR CLASE---------------#
def buscar_clase(request):
    if request.GET["nombre_clase"]: 
        opcion=request.GET.get('nombre_clase')
        context= {"clases":Clase.objects.filter(nombre_clase__icontains=opcion).all()} 
    return render(request, 'Gym/clase.html', context)


#---------------BUSQUEDAS---------------#
def buscar (request):
       nombre = request.GET.get('nombre')
       cliente= Bebida.objects.filter(nombre_bebida__icontains=nombre)

       return render(request, "Gym/resultado_busqueda.html", {"cliente":cliente, "nombre":nombre})
   
def busquedaBebida (request):
    return render (request, "Gym/busqueda_bebida.html")

def mostrar_bebida(request):
    context = {
         "bebidas": Bebida.objects.all(),
         "form": BebidaForm(),
         }
    return render(request, "Gym/padre.html", context)            

def mostrar_otro(request):
    bebidas=Bebida.objects.all()
    return render(request,'Gym/padre.html', {"bebidas": bebidas})
