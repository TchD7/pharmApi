from django.shortcuts import render

from rest_framework import generics
from dashbord.models import Pharms,Pharms_de_garde
from .serializers import PharmsSerializer,Pharms_de_gardeSerializer



class PharmsAPIView(generics.ListAPIView):
    queryset = Pharms.objects.all()
    serializer_class = PharmsSerializer
class Pharms_de_gardeAPIView(generics.ListAPIView):
    queryset = Pharms_de_garde.objects.all()
    serializer_class = Pharms_de_gardeSerializer
