from django.urls import path
from . import views

urlpatterns = [
    path('Register' ,views.Register ,name="Register") ,
    path('Logout' ,views.logout ,name="Logout")
    
]
