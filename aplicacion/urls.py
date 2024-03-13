
from django.urls import path, include
from .views import*

urlpatterns = [
path('', home, name="home"),
path('almacen', almacen, name="almacen"),
path('bebidas', bebida, name="bebidas"),
path('frutas', fruta, name="frutas"),
path('verduras', verdura, name="verduras"),
path('sobre_nos', sobre_nos, name="sobre"),
path('a_l', all_products, name="a_l"),
#Formularios
path('alma_form/', almacen_form,name="alma_form"),
path('bebida_form/', bebida_form,name="bebida_form"),
path('verdura_form/', verdura_form,name="verdura_form"),
path('fruta_form/', fruta_form, name="fruta_form"),

#BuscarProducto
path('buscar_alma/', buscarAlmacen,name="buscar_alma"),
path('encontrar_almacen/', encontrarAlmacen,name="encontrar_almacen"),
]

