from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .api import *

urlpatterns = [
      path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
      path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
      path('api/register', RegisterApi.as_view()),
      path('api/activate/<uidb64>/<token>',activate_account, name='activate'),
      path('api/login', UserLoginView.as_view(), name='login'),
      path('api/doctors', DoctorListView.as_view(), name='doctors'),
      path('api/doctor/<int:docid>',DoctorView.as_view()),
      path('api/patients', PatientListView.as_view(), name='patients'),
      path('api/patient/<int:patid>',PatientView.as_view()),
      path('api/upload-profile', UploadView.as_view()),
]


