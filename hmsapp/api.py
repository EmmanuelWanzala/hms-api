from rest_framework.response import Response
from rest_framework import generics,permissions
from .serializer import AppointmentSerializer
from .models import Appointment

class AppointmentCreateApi(generics.CreateAPIView):
    queryset= Appointment.objects.all()
    serializer_class=AppointmentSerializer

class AppointmentApi(generics.ListAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer

class AppointmentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer

class AppointmentDeleteApi(generics.DestroyAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer