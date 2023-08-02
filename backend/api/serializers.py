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
    user_name = serializers.CharField(
        source='user_id.username', read_only=True)
    user_id = serializers.IntegerField(source='user_id.id', read_only=True)
    work_station_name = serializers.CharField(
        source='workStation_id.station', read_only=True)
    work_station_id = serializers.IntegerField(
        source='workStation_id.id', read_only=True)
    # work_station = WorkStationSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'created_at',
            'updated_at',
            'reservation_date',
            'user_id',
            'work_station_name',
            'work_station_id',
            # 'work_station',
            'user_name',
            ]
