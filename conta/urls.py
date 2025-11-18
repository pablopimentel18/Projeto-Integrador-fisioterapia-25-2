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
    path('paciente/update/<int:paciente_id>/', conta_views.paciente_update, name='update_paciente'),
    path('paciente/delete/<int:paciente_id>/', conta_views.paciente_delete, name='paciente_delete'),
    path('paciente/avaliar/<int:paciente_id>/', conta_views.tipo_avaliacao, name='avaliacao_tipo'),
    path('paciente/avaliar/<int:questionario_id>/primeira_etapa/', conta_views.primeira_etapa_avaliacao, name='avaliar_primeira_etapa'),
    path('paciente/avaliar/<int:questionario_id>/segunda_etapa/', conta_views.segunda_etapa_avaliacao, name='avaliar_segunda_etapa'),
    path('paciente/avaliar/<int:questionario_id>/terceira_etapa/', conta_views.terceira_etapa_avaliacao, name='avaliar_terceira_etapa'),
    path('paciente/avaliar/<int:questionario_id>/quarta_etapa/', conta_views.quarta_etapa_avaliacao, name='avaliar_quarta_etapa'),
    path('paciente/avaliar/<int:questionario_id>/primeira_etapa_obeso/', conta_views.primeira_etapa_avaliacao_obeso, name='avaliar_primeira_etapa_obeso'),
    path('paciente/avaliar/<int:questionario_id>/diagnostico/', conta_views.diagnostico, name='diagnostico'),
    path('paciente/avaliacoes/<int:paciente_id>/', conta_views.questionario_list, name='listar_avaliacoes'),
    path('paciente/avaliar/<int:questionario_id>/diagnostico/pdf/', conta_views.exportar_diagnostico_pdf, name='exportar_diagnostico_pdf'),
]