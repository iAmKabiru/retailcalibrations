from django.contrib import admin
from .models import Calibration

class CalibrationAdmin(admin.ModelAdmin):
    list_display = ('transporter', 'registration_number',
     'calibration_date', 'expiary_date', 
     'chasis_number', 'certificate_number',
     'capacity', 'document', 'status',)

    search_fields = ('transporter', 'registration_number',
     'calibration_date', 'expiary_date', 
     'chasis_number', 'certificate_number',
     'capacity','status',)

    list_per_page = 30
    
admin.site.register(Calibration, CalibrationAdmin)