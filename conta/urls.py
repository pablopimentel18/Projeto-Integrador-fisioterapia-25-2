from django.urls import path
from django.urls import include
from . import views as conta_views


urlpatterns = [
    path('usuario/<int:usuario_id>', conta_views.usuario_read, name='usuario_read'),
    path('create/', conta_views.create_user, name='create_user'),
    path('delete/<int:usuario_id>', conta_views.usuario_delete, name='usuario_delete'),
    path('usuarios/<int:usuario_id>', conta_views.usuario_list, name='usuario_list'),
    path('update/<int:user_id>', conta_views.usuario_update, name='usuario_update'),
    path('sobre/', conta_views.sobre, name='sobre'),
    path('paciente/create/<int:usuario_id>/', conta_views.paciente_create, name='create_paciente'),
    path('paciente/update/<str:paciente_cpf>/', conta_views.paciente_update, name='update_paciente'),
    path('paciente/delete/<str:paciente_cpf>/', conta_views.paciente_delete, name='paciente_delete'),
]