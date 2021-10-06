from django.urls import path

from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('display',views.display,name='display'),
    path('add-donor',views.add_donor,name='add-donor'),
    path('logout',views.logout,name='logout')


]
