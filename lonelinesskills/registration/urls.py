from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('choose_profile_type/', views.choose_profile_type, name='choose_profile_type'),
    path('create_lonely_human_profile/', views.create_lonely_human_profile, name='create_lonely_human_profile'),
    path('create_volunteer_profile/', views.create_volunteer_profile, name='create_volunteer_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]