from django.urls import path
from .views import report_view

app_name = 'report'

urlpatterns = [
    path('report/', report_view, name='report_view'),
]
