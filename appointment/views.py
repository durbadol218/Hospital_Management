from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    
    # custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset() # uporer 7number line ke niye ashlam/ parent ke inherit korlam!
        print(self.request.query_params)
        patient_id = self.request.query_params.get('patient_id') # aitar maddhome patient_id ki niye ashlam!
        if patient_id:
            queryset = queryset.filter(id=patient_id)
        return queryset