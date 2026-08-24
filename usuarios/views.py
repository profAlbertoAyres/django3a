from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import ListView

from usuarios.forms import UsuarioForm, AlunoForm
from usuarios.models import Aluno


# Create your views here.

#FBV
# def lista_alunos(request):
#     alunos = Aluno.objects.all()
#     return render(request,
#                   'usuarios/aluno/lista.html',
#                   {'alunos':alunos})

#CBV
class AlunoListView(ListView):
    model = Aluno
    template_name = 'usuarios/aluno/lista.html'
    context_object_name = 'alunos'


def criar_aluno(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        aluno_form = AlunoForm(request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            try:
                with transaction.atomic():
                    user = user_form.save()
                    aluno = aluno_form.save(commit=False)
                    aluno.user = user
                    aluno.save()
                messages.success(request,'Aluno cadastrado com sucesso!')
                return redirect('usuarios:aluno_lista')
            except Exception:
                messages.error(request,'Não foi possível cadastrar o aluno')

    else:
        user_form = UsuarioForm()
        aluno_form = AlunoForm()
    return render(request, 'usuarios/aluno/form.html',{
            'user_form' : user_form,
            'aluno_form' : aluno_form,
        })
