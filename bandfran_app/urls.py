from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.participant_signup, name='signup'),
    path('signin', views.participant_signin, name='signin'),
    path('signout', views.participant_signout, name='signout'),
    path('callback/', views.participant_callback, name='callback'),
    path('connect', views.participant_connect, name='connect')
]