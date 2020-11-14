from rest_framework import generics, permissions, mixins,status
from rest_framework.response import Response
from .serializer import UserRegistrationSerializer
from .models import CustomUser as User
from rest_framework.permissions import AllowAny, IsAuthenticated

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
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)