from django.contrib import admin
from .models import WorkStation, Reservation, Employee

# Register your models here.

admin.site.register(WorkStation)
admin.site.register(Reservation)
admin.site.register(Employee)
