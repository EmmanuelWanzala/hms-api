from rest_framework.response import Response
from rest_framework import generics,permissions
from .models import *
from .serializer import *
# Create your views here.


class CaseCreateView(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseListSerializer


class CaseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()

class DoctorCaseList(generics.ListAPIView):
    
    serializer_class = CaseListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the cases
        for the doctor.
        """
        queryset = Case.objects.all()
        docid = self.kwargs['docid']
        if docid is not None:
            queryset = queryset.filter(doctor_id=docid)
   
        return queryset  


class PatientCaseList(generics.ListAPIView):
    
    serializer_class = CaseListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the cases
        for the patient.
        """
        queryset = Case.objects.all()
        patid = self.kwargs['patid']
        if patid is not None:
            queryset = queryset.filter(patient_id=patid)
   
        return queryset 
  
  
class AppointmentCreateApi(generics.CreateAPIView):
    queryset= Appointment.objects.all()
    serializer_class=AppointmentSerializer

class AppointmentApi(generics.ListAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentListSerializer

class AppointmentUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer



class DoctorAppointmentList(generics.ListAPIView):
    
    serializer_class = AppointmentListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Appointments
        for the doctor.
        """
        queryset = Appointment.objects.all()
        docid = self.kwargs['docid']
        if docid is not None:
            queryset = queryset.filter(doctor_id=docid)
   
        return queryset  


class PatientAppointmentList(generics.ListAPIView):
    
    serializer_class = AppointmentListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Appointments
        for the patient.
        """
        queryset = Appointment.objects.all()
        patid = self.kwargs['patid']
        if patid is not None:
            queryset = queryset.filter(patient_id=patid)
   
        return queryset 
      
        

class BillApi(generics.ListAPIView):
    queryset=Bill.objects.all()
    serializer_class=BillListSerializer

class BillUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bill.objects.all()
    serializer_class=BillSerializer



class PatientBillList(generics.ListAPIView):
    
    serializer_class = BillListSerializer

    def get_queryset(self):
        """
        This view should return a list of all the bills
        for the patient.
        """
        queryset = Bill.objects.all()
        patid = self.kwargs['patid']
        if patid is not None:
            queryset = queryset.filter(case__patient_id=patid)
   
        return queryset  


