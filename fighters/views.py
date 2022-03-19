# from django.shortcuts import render
from rest_framework import generics
from .serializer import FightersSerializer
from .models import Fighters

class FightersList(generics.ListCreateAPIView):
    # bring in a query set. what are we going to be asking about?
    queryset = Fighters.objects.all()
    # where do we send this conversion data?
    serializer_class = FightersSerializer

class FightersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fighters.objects.all()
    serializer_class = FightersSerializer

# Create your views here.
