from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets as meviewsets
from api.serializers import *
from api.models import *

class WordsViewSet(meviewsets.ModelViewSet):
    # lookup_field = 'id'
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

class TopicsViewSet(meviewsets.ModelViewSet):
    # lookup_field = 'id'
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer

# class ConceptsViewSet(meviewsets.ModelViewSet):
#     lookup_field = 'id'
#     queryset = Concepts.objects.all()
#     serializer_class = ConceptsSerializer

class TweetsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = TweetsSerializer
    queryset = Tweets.objects.all()

class FishViewSet(meviewsets.ModelViewSet):
    lookup_field = 'name'
    serializer_class = FishSerializer
    queryset = Fish.objects.all()
