from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact'),
    path('views/<int:id>', views.views, name='contact_views'),
    path('edit/<int:id>', views.edit, name='contact_edit'),
]
