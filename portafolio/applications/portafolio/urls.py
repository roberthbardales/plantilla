from django.contrib import admin
from django.urls import path
from . import views

app_name = "portafolio_app"
urlpatterns = [
    path('',views.home,name='home'),

]