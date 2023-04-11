from django.contrib import admin
from django.urls import path
from AppCoder import views
from AppCoder.views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    path('cursoformulario/', views.cursoformulario, name='CursoFormulario'),
]
