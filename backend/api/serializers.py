from rest_framework import serializers
from .models import Employee, WorkStation


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}


class WorkStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStation
        fields = "__all__"
