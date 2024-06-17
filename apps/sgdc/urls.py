from django.urls import path
from . import views

app_name = 'sgdc'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_briefing, name='new_briefing'),
    path('edit/<int:pk>/', views.edit_briefing, name='edit_briefing'),
    path('delete/<int:pk>/', views.delete_briefing, name='delete_briefing'),
    path('week/', views.week_briefings_list, name='week_briefings_list'),
    path('week/<int:year>/<int:week>/', views.week_briefings_detail, name='week_briefings_detail'),
]
