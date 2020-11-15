from rest_framework import  serializers
from .models import Case
from users.models import CustomUser as User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','role', 'email')   

class CaseListSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True, many=False)
    doctor = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Case
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'        



  

