from django.db import models
from users.models import CustomUser as User
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


class Medication(models.Model): 
    """
    Medication class to define medication Objects
    """
  
    med_name = models.CharField(max_length =100)
    med_cost_price = models.PositiveIntegerField()
    med_manufacture = models.CharField(max_length =100)
    med_description = models.TextField()


    def __str__(self):
        return self.med_name




class Service(models.Model): 
    """
    Service class to define service Objects
    """
  
    service_name = models.CharField(max_length =100)
    service_cost = models.PositiveIntegerField()
    service_description = models.TextField()


    def __str__(self):
        return self.service_name        

class Case(models.Model): 
    """
    Case class to define case Objects
    """
    patient = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='case_patient')
    doctor = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='case_doctor')
    case_title = models.CharField(max_length =150)
    diagnosis = models.TextField()
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE,null=True,blank=True)
    medication_quantity=models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,null=True,blank=True)
    admission_days = models.PositiveIntegerField(default=0)
    case_date = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f'{self.case_title}:{self.patient_id}:{self.diagnosis}'        

class Bill(models.Model):
    """
    Bill class to define bill Objects
    """
    
    case = models.OneToOneField(Case, on_delete=models.CASCADE)
    admission_fee = models.PositiveIntegerField(default=0)
    service_fee =   models.PositiveIntegerField(default=0)
    medication_fee = models.PositiveIntegerField(default=0)
    doc_fee = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    bill_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return f'{self.case.case_title}:{self.total_amount}:{self.is_paid}'  





    

   

  