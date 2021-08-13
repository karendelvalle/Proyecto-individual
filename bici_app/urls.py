from django.urls import path
from .import views

urlpatterns = [
    path('', views.cicletealo),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('ejemplo', views.ejemplo),
    path('cicletealo', views.cicletealo),
    path('delete', views.delete),
    path('add_evento', views.add_evento),
    path('crear_evento', views.crear_evento),
    path('editar/<int:id>', views.editar_evento),
    path('user', views.user),
    path('remover_evento', views.remover_evento),
    path('mensajes/<int:id>', views.mensajes),
    path('comentar_mensaje/<int:id>', views.comentar_mensaje),
    path('imprimir/<int:id>', views.imprimir),
    path('delete/<int:id>', views.delete_mensaje) 
]