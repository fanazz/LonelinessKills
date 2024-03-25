from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register_volunteer/', views.register_as_volunteer, name='register_as_volunteer'),
    path('register_lonely_human/', views.register_as_lonely_human, name='register_as_lonely_human'),
    path('detail/', views.user_detail, name='user_detail_current'),
    path('detail/<str:username>/', views.user_detail, name='user_detail'),
    path('user_update/', views.volunteer_additional_information, name='user_update')
    # path('lonely/', views.create_lonelyhuman, name='lonely'),
    #path('register/', views.register, name='register'),
    #path('choose_profile_type/', views.choose_profile_type, name='choose_profile_type'),
    #path('create_lonely_human_profile/', views.create_lonely_human_profile, name='create_lonely_human_profile'),
    #path('create_volunteer_profile/', views.create_volunteer_profile, name='create_volunteer_profile'),
]