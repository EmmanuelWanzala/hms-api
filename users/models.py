from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):

    # These fields tie to the roles!
    ADMIN = 1
    DOCTOR = 2
    PATIENT = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient')
    )

    username = None
    email = models.EmailField(('email address'), unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



departments=[('Consultant','Consultant'),
('Cardiologist','Cardiologist'),
('Oncologist','Oncologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Consultant')
 
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)


