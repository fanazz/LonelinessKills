from django.urls import path
from . import views

urlpatterns = [
    # path('', views.signup, name='index'),
    # path('signup', views.signup, name='signup'),
    path('volunteers', views.volunteer_list, name='volunteer_list'),
    path('lonelyhuman', views.lonely_human_list, name='lonely_human_list'),
]
