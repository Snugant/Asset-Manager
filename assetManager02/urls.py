"""
assetManager02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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
from django.urls import path
from AssetManagerApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.homepage, name=""),
    
    path('register', views.register, name="register"),

    path('login', views.login, name="login"),
    
    path('dashboard', views.dashboard, name="dashboard"),

    path('logout', views.logout, name="logout"),
    
    path('new-item/<int:space_id>/', views.newItem, name="newItem"),
    
    path('edit-item/<int:log_id>/<int:space_id>/', views.editItem, name="editItem"),
     
    path('delete-item/<int:log_id>/<int:space_id>/', views.deleteItem, name="deleteItem"),
    
    path('edit-space/<int:space_id>/', views.editSpace, name='editSpace'),
    
    path('create-space', views.createSpace, name='createSpace'),

    path('delete-space/<int:space_id>/', views.deleteSpace, name='deleteSpace'),
    
    path('dashboard/<int:space_id>/', views.dashboard, name= 'dashboard'),
    
    path('settings', views.settings, name='settings'),
    
]
