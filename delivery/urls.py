from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('open_signup/',views.open_signup,name='open_sinup'),
    path('open_signin/',views.open_signin,name='open_signin'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signin/open_add_dress',views.open_add_dress,name='open_add_dress'),
    path('add',views.add,name='add'),
]