
from django.urls import path 
from .views import *
urlpatterns = [
    path('Proflie/' , index ,name="Profile")
]
