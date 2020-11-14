from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi,activate_account
urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('activate/<uidb64>/<token>',activate_account, name='activate'),
]