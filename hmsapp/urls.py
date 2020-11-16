from django.urls import path
from .api import *


urlpatterns = [
    path('api/case/create',CaseCreateView.as_view()),#create case
    path('api/cases',CaseListView.as_view()),#view all cases
    path('api/case/<int:pk>',CaseView.as_view()),#update,view or delete one case
    path('api/cases/doctor/<int:docid>',DoctorCaseList.as_view()),#view all doctor cases
    path('api/cases/patient/<int:patid>',PatientCaseList.as_view()),#view all patient cases

    path('api/appointment/create',AppointmentCreateApi.as_view()),#create appointment
    path('api/appointments',AppointmentApi.as_view()),#view all appointments
    path('api/appointment/<int:pk>',AppointmentUpdateApi.as_view()),#update,view or delete appointment
    path('api/appointments/doctor/<int:docid>',DoctorAppointmentList.as_view()),#view all doctor appointment
    path('api/appointments/patient/<int:patid>',PatientAppointmentList.as_view()),#view all patient appointment
    
    path('api/bills',BillApi.as_view()),#view all bills
    path('api/bill/<int:pk>',BillUpdateApi.as_view()),#update,view or delete bill
    path('api/bills/patient/<int:patid>',PatientBillList.as_view()),#view all bills by pa
    
    path('api/medication/create',MedicationCreateApi.as_view()),
    path('api/medication',MedicationApi.as_view()),
    path('api/medication/<int:pk>',MedicationUpdateApi.as_view()),
    path('api/medication/<int:pk>/delete',MedicationDeleteApi.as_view()),

    path('api/service/create',ServiceCreateApi.as_view()),
    path('api/service',ServiceApi.as_view()),
    path('api/service/<int:pk>',ServiceUpdateApi.as_view()),
    path('api/service/<int:pk>/delete',ServiceDeleteApi.as_view()),    
    

]

