from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import WorkStationSerializer, ReservationSerializer
from .models import WorkStation, Reservation
from django.http import JsonResponse
import json
from rest_framework.permissions import IsAuthenticated
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.permissions import AllowAny

# Create your views here.


@api_view(['GET'])
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'X-CSRFToken': token})


@api_view(['POST'])
@csrf_protect
def login_user(request):
    if request.method == 'POST':
        try:
            data = request.data
            email = data['email']
            password = data['password']
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid request body'})

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return JsonResponse({'access_token': access_token})
            else:
                return JsonResponse({'error': 'Invalid email or password'})
        else:
            return JsonResponse({'error': 'Missing email or password'})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_stations(request):
    stations = WorkStation.objects.all()
    serialized_stations = WorkStationSerializer(stations, many=True)
    return Response(serialized_stations.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        request.session.flush()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_reservations(request):
    print(request.user.id)
    reservations = Reservation.objects.filter(user_id=request.user)
    serialized_reservations = ReservationSerializer(reservations, many=True)
    return Response(serialized_reservations.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
# @permission_classes([AllowAny])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
# @csrf_protect
def post_reservation(request):
    data = {
        'user_id': request.user.id,
        'user_name': request.user.username,
        'reservation_date': request.data.get('reservation_date', None),
        'work_station_id': request.data.get('work_station_id', None),
        'work_station_name': request.data.get('work_station_name', None),
    }
    print(data)
    serialized_reservation = ReservationSerializer(data=data)
    if serialized_reservation.is_valid():
        serialized_reservation.save()
        return Response(status=status.HTTP_201_CREATED)

    print(serialized_reservation.errors)
    return Response(
        serialized_reservation.errors, status=status.HTTP_400_BAD_REQUEST)
