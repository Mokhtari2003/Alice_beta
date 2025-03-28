"""
URL configuration for Alice_Register project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path ,include
from Register import urls as Register_Urls
from Ai_service_Home import urls as Home_urls
from Profile import urls as Profile_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(Register_Urls)),
    path('' ,include(Home_urls)) ,
    path('' ,include(Profile_urls))
]
