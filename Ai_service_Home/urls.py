from django.urls import path
from . import views
from Register.views import logout_views

urlpatterns = [
    path('' ,views.Home ,name="Home") ,
    path('logout' , logout_views , name="Logout")
]
