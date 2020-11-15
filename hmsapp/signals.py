from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Case,Bill

@receiver(post_save, sender=Case)
def create_bill_signal(sender, instance, created, **kwargs):
    if created:
        adm_fee=int(instance.admission_days*500)
        s_fee=0
        med_fee=0
        doc_fee=1000
        if instance.service:
            s_fee=int(instance.service.service_cost)
        if instance.medication:
            med_fee=int((instance.medication.med_cost_price)*instance.medication_quantity)
        total_amount=int(adm_fee+s_fee+med_fee+doc_fee)
        Bill.objects.create(case=instance,admission_fee=adm_fee,service_fee=s_fee,medication_fee=med_fee,doc_fee=doc_fee,total_amount=total_amount)
        
        instance.bill.save()
