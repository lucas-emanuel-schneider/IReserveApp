from django.contrib.auth.backends import BaseBackend
from .models import Employee


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Employee.objects.get(email=email)
            #  problemas na autenticação nesse ponto devido a model custom
            #  deixei sem o hash já que ainda não consegui solucionar
            print('testando dentro do auth', user.check_password(password))
            if user.password == password:
                return user
            else:
                print("Invalid password for user:", email)
        except Employee.DoesNotExist:
            print("User not found:", email)

        return None
