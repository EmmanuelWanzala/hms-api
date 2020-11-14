from rest_framework import  serializers
from django.db import models
from .models import CustomUser as User
from django.contrib.auth.hashers import make_password
# Register serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','role','first_name', 'last_name','address','mobile','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      return user