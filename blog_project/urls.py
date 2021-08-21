"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from blog.api import user_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    # Basically it’s just a view to receive a POST request with username and password.
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include('blog.urls')),
    # Here is the path to remove current user's token - logout action
    path('api-token-logout/', user_logout, name='api-token-logout'),
]
