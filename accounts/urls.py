from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signout', views.signout,name='signout'),


]
