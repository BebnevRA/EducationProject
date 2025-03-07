from django.urls import path

from . import views

app_name = 'reminder'
urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('<int:note_id>/', views.note, name='note'),
    path('note_add', views.note_add, name='note_add')
]
