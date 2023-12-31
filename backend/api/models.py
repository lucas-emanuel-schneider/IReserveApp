from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField("Created", auto_now_add=True)
    updated_at = models.DateTimeField("Updated", auto_now_add=True)

    class Meta:
        abstract = True


class Account_Manager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser, Base):
    address = models.CharField(
        "address", max_length=255, null=False, blank=False)
    email = models.EmailField(
        "email", max_length=255, null=False, blank=False, unique=True)
    mobile = models.CharField("phone", max_length=255, null=False, blank=False)
    username = models.CharField(
        "username", max_length=255, null=False, blank=False, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = Account_Manager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


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
        null=False, blank=False,
    )
    reservation_date = models.DateField(null=False, blank=False)
    work_station = models.ForeignKey(
        WorkStation,
        on_delete=models.CASCADE,
        null=False, blank=False)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        username = self.user.username
        return f"Reservation for {username}, {self.reservation_date}"
