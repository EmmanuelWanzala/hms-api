from django.contrib import admin
from .models import Appointment,Medication,Service,Case
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Service)
admin.site.register(Case)

