from django.test import TestCase
from .models import Service
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse 
from .serializer import *

# Create your tests here.
class ServiceTestClass(TestCase):

    # Set up method
    def setUp(self):

        """Define the test client and other test variables."""

        self.new_service=Service(service_name='X-ray',service_cost=500,service_description='Xray test')
        
    def test_model_can_create_a_service(self):

        """Test the service model can create a service."""

        self.new_service.save()
        count = Service.objects.count()
        self.assertTrue(count == 1)

    # Testing  instance

    def test_instance(self):

        self.assertTrue(isinstance(self.new_service,Service))    


