from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('insert',views.insert,name='insert'),
    path('Signup',views.Signup,name='Signup'),
    path('register',views.register,name='register'),
    path('Login',views.login,name='login'),
]