from django.urls import path
from . import views

app_name = 'clima_espacial'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_clima, name='new_clima'),
    path('edit/<int:pk>/', views.edit_clima, name='edit_clima'),
    path('delete/<int:pk>/', views.delete_clima, name='delete_clima'),
]
