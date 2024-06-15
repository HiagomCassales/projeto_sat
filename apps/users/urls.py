# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('sgdc/', views.sgdc_view, name='sgdc_view'),
    path('lessonia/', views.lessonia_view, name='lessonia_view'),
    path('infraestruturas_criticas/', views.infraestruturas_criticas_view, name='infraestruturas_criticas_view'),
]
