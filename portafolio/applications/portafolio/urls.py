from django.contrib import admin
from django.urls import path
from . import views

from .import views

app_name = "portafolio_app"
urlpatterns = [

 path(
        '',
        views.PaginaInicio.as_view(),
        name="home"
    ),
  path(
        'listar_proyecto/',
        views.ListarProyecto.as_view(),
        name="listar_proyecto"
    ),
    path(
        'detalle_proyecto/<pk>',
        views.ProyectoDetailView.as_view(),
        name="detalle_proyecto"
    ),
    path(
        'agregar_proyecto/',
        views.ProyectoCreateView.as_view(),
        name="agregar_proyecto"
    ),
    path(
        'eliminar_proyecto/<pk>',
        views.ProyectoDeleteView.as_view(),
        name="eliminar_proyecto"
    ),
    path(
        'modificar_proyecto/<pk>',
        views.ProyectoUpdateView.as_view(),
        name="modificar_proyecto"
    ),
    path(
        'buscar_proyecto/',
        views.ListarProyectoByKword.as_view(),
        name='buscar_proyecto',
    ),
# ---------------P R U E B A S-----------------------
    path(
        'proyecto_etiqueta/<int:etiqueta_id>/',
        views.ProyectosPorEtiquetaListView.as_view(),
        name='proyectos_por_etiqueta'
    ),
    path('etiqueta/<int:pk>/',  #    path('etiqueta/<pk>/',
         views.EtiquetaDetailView.as_view(),
         name='etiqueta_detail'),

# ---------------P R U E B A S-----------------------



]



#     path(
#         'autores',
#         views.ListarAutores2.as_view(),
#         name="autores"
#     ),
#     path(
#         'buscar-autores/',
#         views.BuscarAutor.as_view(),
#         name="buscar-autores"
#     ),









    # basado en funciones
    # path('',views.home,name='home'),
    # path('add',views.add,name='add'),
    # path('list',views.list,name='list'),
    # # path('add2',views.add2,name='add2'),
    # path('update',views.update,name='update'),
    # path('delete',views.delete,name='delete'),