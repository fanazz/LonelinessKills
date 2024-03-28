from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register_volunteer/', views.register_as_volunteer, name='register_as_volunteer'),
    path('register_lonely_human/', views.register_as_lonely_human, name='register_as_lonely_human'),
    path('detail/', views.user_detail, name='user_detail_current'),
    path('detail/<str:username>/', views.user_detail, name='user_detail'),
    #path('register/', views.register, name='register'),

]