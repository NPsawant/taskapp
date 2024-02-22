from django.urls import path
from authapp import views

urlpatterns = [
    path('register',views.user_register),
     path('login',views.user_login),

]   