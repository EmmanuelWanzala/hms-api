from django.urls import path
from .api import *


urlpatterns = [
    path('api/case/create',CaseCreateView.as_view()),#create case
    path('api/cases',CaseListView.as_view()),#view all cases
    path('api/case/<int:pk>',CaseView.as_view()),#update,view or delete one case
    path('api/cases/doctor/<int:docid>',DoctorCaseList.as_view()),#view all doctor cases
    path('api/cases/patient/<int:patid>',PatientCaseList.as_view()),#view all patient cases
    path('api/appointment/create',AppointmentCreateApi.as_view()),
    path('api/appointment',AppointmentApi.as_view()),
    path('api/appointment/<int:pk>',AppointmentUpdateApi.as_view()),
    path('api/appointment/<int:pk>',AppointmentDeleteApi.as_view()),

]

