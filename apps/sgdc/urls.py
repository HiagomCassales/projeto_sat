from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_espacial_segment, name='create_espacial_segment'),
]
