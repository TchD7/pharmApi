from django.urls import path
from .views import PharmsAPIView,Pharms_de_gardeAPIView
urlpatterns = [
path('', PharmsAPIView.as_view()),
path('garde/',Pharms_de_gardeAPIView.as_view()),
]