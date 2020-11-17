from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import render,redirect,reverse
from rest_framework import generics, permissions, mixins,status
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token_generator import account_activation_token
from .serializer import UserRegistrationSerializer,UserLoginSerializer
from .models import CustomUser as User


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered.Verify email address to activate account!',
                'user': serializer.data
            }

            return Response(response, status=status_code)

#Account activation API
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        login(request, user)
        context={
        'success':True,
        'status':'success',
        'message':'Your account has been activated successfully',
        }
        return render(request,'activation_status.html',context)
    else:
        context={
        'success':False,
        'status':'danger',
        'message':'Activation link is invalid!',
        }
        return render(request,'activation_status.html',context)       



#Login API
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)        