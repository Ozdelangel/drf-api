# from django.shortcuts import render
from rest_framework import generics
from .serializer import FightersSerializer
from .models import Fighters
from .permissions import IsOwnerOrReadOnly

class FightersList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    # bring in a query set. what are we going to be asking about?
    queryset = Fighters.objects.all()
    # where do we send this conversion data?
    serializer_class = FightersSerializer

class FightersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Fighters.objects.all()
    serializer_class = FightersSerializer

# Create your views here.
