from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact'),
    path('view/<int:id>', views.view, name='contact_view'),
    path('delete/<int:id>', views.delete, name='contact_delete'),
    path('edit/<int:id>', views.edit, name='contact_edit'),
]
