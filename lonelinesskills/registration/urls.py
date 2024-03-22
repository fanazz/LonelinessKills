from django.urls import path
from . import views

urlpatterns = [
    # path('', views.signup, name='index'),
    # path('signup', views.signup, name='signup'),
    path('registration/registerlonelyhuman/', views.lonely_human_register, name='lonely_human_register'),
    path('registration/lonelyhumanprofile/', views.lonely_human_fill_information, name='lonely_human_fill_information'),
    path('registration/registervolunteer/', views.lonely_human_register, name='volunteer_register'),
    path('registration/volunteerprofile/', views.lonely_human_fill_information, name='volunteer_fill_information'),
    path('volunteers', views.volunteer_list, name='volunteer_list'),
    path('lonelyhuman', views.lonely_human_list, name='lonely_human_list'),
]
