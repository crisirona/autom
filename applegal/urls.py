from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.Index,name='index'),
    path('creardemanda/',views.NuevaDemanda,name='creardemanda'),
    path('about/',views.About,name='about'),
    path('base/',views.Base,name='base'),
    path('login/', views.AdminLogin.as_view(), name="login"),
    path('logout/', login_required(views.AdminLogout.as_view()), name="logout"),
    path('register/',views.register,name='register'),
    path('crud/',views.crud, name='crud'),
    path('busqueda/',login_required(views.busqueda),name='busqueda'),
    path('contact/',views.contact,name='contact'),
    path('modlista/',views.listaCasosAction,name='modlista'),
    path('elilista/',views.listaCasosAction2,name='elilista'),
    path('modificar/<int:id>/',views.editar,name='modificar'),
    path('eliminar/<int:id>/',views.eliminarconf,name='eliminar'),

]
