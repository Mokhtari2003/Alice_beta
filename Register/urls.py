from django.urls import path ,include
from . import views
urlpatterns = [
    path('Register' ,views.Register ,name="Register") ,
    path('Logout' ,views.logout ,name="Logout") ,
    path('google/', include('allauth.urls')),
    
]
