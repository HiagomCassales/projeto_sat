"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('', user_views.login_view, name='login'),
    path('post_login_redirect/', user_views.post_login_redirect, name='post_login_redirect'),
    path('sgdc/', include('apps.sgdc.urls', namespace='sgdc')),
    path('lessonia/', include('apps.lessonia.urls', namespace='lessonia')),
    path('infraestruturas_criticas/', include('apps.infraestrutura_critica.urls', namespace='infraestrutura_critica')),
]


