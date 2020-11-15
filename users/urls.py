from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .api import RegisterApi,activate_account,UserLoginView

urlpatterns = [
      path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
      path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
      path('api/register', RegisterApi.as_view()),
      path('api/activate/<uidb64>/<token>',activate_account, name='activate'),
      path('api/login', UserLoginView.as_view(), name='login'),
]


