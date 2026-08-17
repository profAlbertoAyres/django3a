from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    #FBV
    # path('alunos/',views.lista_alunos, name='aluno_lista'),
    #CBV
    path('alunos/',views.AlunoListView.as_view(),name='aluno_lista'),

]