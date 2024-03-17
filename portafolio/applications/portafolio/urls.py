from django.contrib import admin
from django.urls import path
from . import views

app_name = "portafolio_app"
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('list',views.list,name='list'),
    # path('add2',views.add2,name='add2'),
    path('update',views.update,name='update'),
    path('delete',views.delete,name='delete'),

]