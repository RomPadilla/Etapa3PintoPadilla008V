from django.urls import path
from . import views

urlpatterns=[
    path('',views.user,name='User'),
    path('FormularioRegistro/', views.formularioRegistro, name="register"),
    path('modificarUser/<id>/', views.modificarUser, name='modificarUser'),
    path('eliminarUser/<id>/', views.eliminarUser, name='eliminarUser'),
]
