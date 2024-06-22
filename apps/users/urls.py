# apps/users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject_user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('change_category/<int:user_id>/', views.change_category, name='change_category'),
    path('sgdc/', views.sgdc_view, name='sgdc_view'),
    path('lessonia/', views.lessonia_view, name='lessonia_view'),
    path('infraestruturas_criticas/', views.infraestruturas_criticas_view, name='infraestruturas_criticas_view'),
    path('clima_espacial/', views.clima_espacial_view, name='clima_espacial_view'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
