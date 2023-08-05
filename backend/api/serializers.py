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
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
    )
    work_station_id = serializers.PrimaryKeyRelatedField(
        queryset=WorkStation.objects.all(),
    )
    work_station_name = serializers.StringRelatedField(
        source='work_station.station', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'created_at',
            'updated_at',
            'reservation_date',
            'user_id',
            'work_station_id',
            'work_station_name',
        ]

    def create(self, validated_data):
        print(validated_data['work_station_id'].id, 'AAAAAAAAAAAAAAAAAAAAAA')
        data_format = {
            'user_id': validated_data['user_id'].id,
            'work_station_id': validated_data['work_station_id'].id,
            'reservation_date': validated_data["reservation_date"],
        }
        return Reservation.objects.create(**data_format)
