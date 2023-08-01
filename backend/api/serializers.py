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
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    workStation = WorkStationSerializer()

    class Meta:
        model = Reservation
        fields = [
            'id',
            'created_at',
            'updated_at',
            'reservation_date',
            'user_id',
            'workStation',
            'user_name',
            ]
