from django.shortcuts import render


def Index(request):
    
    return render(request, 'applegal/index.html')

def NuevaDemanda(request):

    contexto={

    }

    return render(request,'applegal/sidebar-left.html',contexto)

def About(request):
    
    return render(request, 'applegal/about.html')