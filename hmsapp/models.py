from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Appointment(models.Model): 
    """
    Appointment class to define appointment Objects
    """
    patient = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='app_patient')
    doctor = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='app_doctor')
    app_title = models.CharField(max_length =150)
    app_details = models.TextField()
    app_status = models.IntegerField(default=0) 
    app_date = models.DateTimeField()
   

    def __str__(self):
        return self.app_title







    

   

  