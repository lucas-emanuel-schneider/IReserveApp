from django.contrib.auth.backends import BaseBackend
from .models import Employee


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Employee.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                print("Invalid password for user:", email)
        except Employee.DoesNotExist:
            print("User not found:", email)

        return None
