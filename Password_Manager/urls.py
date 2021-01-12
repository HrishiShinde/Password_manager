"""Password_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from PMapp import views as pm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logshow/', pm.logshow),
    path('login/',pm.dologin),
    path('regshow/', pm.regshow),
    path('register/',pm.doregister),
    path('showAddPass/', pm.showap),
    path('store/',pm.storepass),
    path('genp/',pm.genpass),
]
