from django.urls import path
from . import views

app_name = 'contratos_imagens'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_contrato, name='new_contrato'),
    path('edit/<int:pk>/', views.edit_contrato, name='edit_contrato'),
    path('delete/<int:pk>/', views.delete_contrato, name='delete_contrato'),
]
