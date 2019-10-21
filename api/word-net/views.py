from django.shortcuts import render
from rest_framework import viewsets
from .models import WordNet
from .serializers import WordNetSerializer
# Create your views here.

class WordNetViewSet(viewsets.ModelViewSet):
    queryset = WordNet.objects.all()
    serializer_class = WordNetSerializer

