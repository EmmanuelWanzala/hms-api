from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser,Doctor,Patient
from .send_confirm_email import send_confirmation_email
@receiver(post_save, sender=CustomUser)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        if instance.role==2:
            Doctor.objects.create(user=instance)
            instance.doctor.save()
            send_confirmation_email(instance)
        elif instance.role==3:
            Patient.objects.create(user=instance)
            instance.patient.save()
            send_confirmation_email(instance)  