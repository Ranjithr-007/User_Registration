from django.urls import path
from . import views
from .views import *

urlpatterns=[
        path('',views.welcome,name="welcome"),
        path('home',views.home,name="home"),
        path("login", login_view, name="login"),
        path("signup", signup_view, name="signup"),
        path("data_view", data_view, name="data_view"),
        path("delete",delete,name="delete"),


]
