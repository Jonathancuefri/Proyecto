from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/<str:tipo>/', views.formulario, name="formulario"),
    path('read/<str:tabla>/', views.lectura_general, name='lectura_general'),
    path('read/<str:tabla>/<str:nombre>/', views.lectura_personal, name='lectura_personal'),
    path('update/<str:tabla>/<str:nombre>/', views.update_registro, name='update_registro'),
    path('delete/<str:tabla>/<str:nombre>/', views.delete_registro, name='delete_registro'),
    path('hoja_devolucion/empleados/<str:nombre>/', views.hoja_devolucion, name='hoja_devolucion')
]