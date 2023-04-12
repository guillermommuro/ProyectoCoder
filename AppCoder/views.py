from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def inicio(request):

    return render(request, 'incio.html')

def cursos(request):

    return render(request, 'cursos.html')

def profesores(request):

    return render(request, 'profesores.html')

def estudiantes(request):

    return render(request, 'estudiantes.html')

def entregables(request):

    return render(request, 'entregables.html')

def cursoformulario(request):

    # print('method: ', request.method)
    # print('post: ', request.post)

    # if request.method == 'POST':    

    #     miformulario = cursoformulario(request.POST)

    #     print(miformulario)

    #     if miformulario.is_valid:

    #         informacion = miformulario.cleaned_data

    #         Curso = curso (nombre=request.post['curso'], camada=request.post['camada'])

    #         Curso.save()

    #         return render(request, 'inicio.html' )

    # else:

    #     miformulario = cursoformulario()

    return render(request, 'cursoformulario.html')
        

        
        

        

