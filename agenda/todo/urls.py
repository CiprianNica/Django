from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('create/', views.create, name='todo_create'),
    path('views/<int:id>', views.view, name='todo_view'),
    path('edit/<int:id>', views.edit, name= 'todo_edit'),
    path('delete/<int:id>', views.delete, name='todo_delete'),
]
