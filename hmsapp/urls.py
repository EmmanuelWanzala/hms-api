from django.urls import path
from .api import AppointmentCreateApi,AppointmentApi, AppointmentDeleteApi,AppointmentUpdateApi

# from .api import AppointmentAPI

urlpatterns = [
      path('api/appointment/create',AppointmentCreateApi.as_view()),
      path('api/appointment',AppointmentApi.as_view()),
      path('api/appointment/<int:pk>',AppointmentUpdateApi.as_view()),
      path('api/appointment/<int:pk>',AppointmentDeleteApi.as_view()),


    # path('api/appointment',ScheduleAPI.as_view()),
    
]

