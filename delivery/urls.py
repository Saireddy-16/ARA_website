from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('open_signup/',views.open_signup,name='open_sinup'),
    path('open_signin/',views.open_signin,name='open_signin'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signin/open_add_dress/',views.open_add_dress,name='open_add_dress'),
    path('add/',views.add,name='add'),
    path('add/update_dress/<int:dress_id>',views.update_dress,name='update_dress'),
    path('dress_update/<int:dress_id>/',views.dress_update,name='dress_update'),
    path('add/delete_dress/<int:dress_id>',views.dress_delete,name='delete_dress'),
    path('signin/display_dresses/',views.display_dresses,name='display_dresses'),
]