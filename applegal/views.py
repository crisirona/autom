from django.shortcuts import redirect, render
from .forms import  DemandaForm,NewUserForm
from .models import Demanda
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.contrib import messages



def Index(request):
    
    return render(request, 'applegal/index.html')

def NuevaDemanda(request):
    if request.method == 'POST':
        demanda = DemandaForm(request.POST)
        
        if demanda.is_valid() :
            dem=demanda.save(commit=False)
            dem.author= request.user
            dem.save()
            messages.success(request, "Guardado correctamente")
            return redirect('index')
    else:
        demanda = DemandaForm()

    contexto={
        'demanda':demanda, 
    }

    return render(request,'applegal/sidebar-left.html',contexto)

def About(request):
    
    return render(request, 'applegal/about.html')

def Base(request):
    
    return render(request, 'applegal/base.html')


def register(request):
    if request.method == 'POST':  
        form = NewUserForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('index')
    else:  
        form = NewUserForm()  
    context = {  
        'form':form  
    }  
    return render(request,'applegal/accounts/signup.html',context)


class AdminLogin(LoginView):
    template_name = 'applegal/accounts/signin.html'


class AdminLogout(LogoutView):
    pass

def crud(request):
    demanda = Demanda.objects.all()

    contexto={
        'demanda':demanda,

    }
    return render(request,'applegal/crud.html',contexto)

def busqueda(request):
    busqueda = request.GET.get("buscar")
    demanda = Demanda.objects.all()
    if busqueda:
        demanda = Demanda.objects.filter(
            Q(id_demanda__icontains= busqueda)
        ).distinct()
        
    
    contexto={
        'demanda':demanda,
        
    }
    return render(request,'applegal/buscar.html',contexto)

def contact(request):
    return render(request,'applegal/contact.html')


def listaCasosAction(request):
    casos = Demanda.objects.all()
    contexto = {
        'casos': casos
    }
    return render(request,'applegal/modificarlista.html',contexto)

def editar(request,id):
    demanda = Demanda.objects.get(id=id)
    formulario = DemandaForm(request.POST or None, request.FILES or None, instance=demanda)
    if request.method == "POST":
        form = DemandaForm(request.POST or None, request.FILES or None, instance=demanda)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = DemandaForm( instance=demanda)
    contexto={
        'demanda':demanda,
        'formulario':form
    }
    return render(request,'applegal/modificar.html',contexto)


def eliminar(request,id):
    demanda=Demanda.objects.get(id=id)
    demanda.delete()
    return redirect('elilista')

def listaCasosAction2(request):
    casos = Demanda.objects.all()
    contexto = {
        'casos': casos
    }
    return render(request,'applegal/eliminarlista.html',contexto)

def eliminarconf(request,id):
    demanda=Demanda.objects.get(id=id)
    contexto={
        'caso':demanda,
    }
    return render(request,'applegal/elminar.html',contexto)