from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('creardemanda/',views.NuevaDemanda,name='creardemanda'),
    path('about/',views.About,name='about'),
]
