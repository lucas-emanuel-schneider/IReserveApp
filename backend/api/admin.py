from django.contrib import admin
from .models import WorkStation, Reservation, Employee


admin.site.register(Employee)
admin.site.register(WorkStation)
admin.site.register(Reservation)
