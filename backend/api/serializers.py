from rest_framework import serializers
from .models import Employee, WorkStation, Reservation


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}


class WorkStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStation
        fields = ['id', 'station']


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        write_only=True
    )
    work_station = serializers.PrimaryKeyRelatedField(
        queryset=WorkStation.objects.all(),
        write_only=True
    )

    class Meta:
        model = Reservation
        fields = [
            'id',
            'created_at',
            'updated_at',
            'reservation_date',
            'user',
            'work_station',
        ]
