from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all() #model theke data guloke query kore niye ashbo!
    serializer_class = serializers.ServiceSerializer # query kora data ke json a convert korbe ai line er maddhome!