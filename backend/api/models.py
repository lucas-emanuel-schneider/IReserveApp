from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField("Created", auto_now_add=True)
    updated_at = models.DateTimeField("Updated", auto_now_add=True)

    class Meta:
        abstract = True


class Employee(AbstractUser):
    phone = models.CharField("phone", max_length=255, null=False, blank=False)
    address = models.CharField(
        "address", max_length=255, null=False, blank=False)


class WorkStation(Base):
    station = models.CharField(
        "station", max_length=100, null=False, blank=False, unique=True)
    available = models.BooleanField(null=False, blank=False)

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"

    def __str__(self):
        return self.station


class Reservation(Base):
    user = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        to_field='id', related_name='user',
        null=False, blank=False,
    )
    reservation_date = models.DateField(
        "reservation_date", null=False, blank=False)
    workStation = models.ForeignKey(
        WorkStation,
        on_delete=models.CASCADE,
        to_field='id', related_name='workStation',
        null=False, blank=False)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f"Reservation for {self.user}, {self.reservation_date}"
