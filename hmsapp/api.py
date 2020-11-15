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

        