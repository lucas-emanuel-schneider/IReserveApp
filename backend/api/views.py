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
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


# @ensure_csrf_cookie não consegui setar o cookie na resposta
@api_view(['GET'])
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'X-CSRFToken': token})


@api_view(['POST'])
# @csrf_protect não consegui fazer funcionar...
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
                user_response = {
                    "id": user.id,
                    "email": user.email, "username": user.username}
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return JsonResponse({
                    'access_token': access_token, "user": user_response})
            else:
                return JsonResponse({
                    'error': 'Invalid email or password'}, status=400)
        else:
            return JsonResponse({
                'error': 'Missing email or password'}, status=405)


@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
@csrf_exempt
def get_stations(request):
    stations = WorkStation.objects.filter(available=True)
    serialized_stations = WorkStationSerializer(stations, many=True)
    return Response(serialized_stations.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        request.session.flush()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
# @authentication_classes([JWTAuthentication]) precisa consertar isso aqui!
@csrf_exempt
# @permission_classes([AllowAny])
def get_reservations(request, user_id):
    reservations = Reservation.objects.filter(user_id=user_id)
    serialized_reservations = ReservationSerializer(reservations, many=True)
    return Response(serialized_reservations.data, status=status.HTTP_200_OK)


@api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# @csrf_protect não consegui fazer funcionar...
@csrf_exempt
def post_reservation(request):
    print(request.data, 'DATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    data = {
        'user_id': int(request.data['user_id']),
        'reservation_date': request.data['reservation_date'],
        'work_station_id': int(request.data['work_station_id']),
    }
    serialized_reservation = ReservationSerializer(data=data)
    # print(serialized_reservation, 'SERIALIZED_RESERVATION')
    if serialized_reservation.is_valid():
        serialized_reservation.save()
        return Response(status=status.HTTP_201_CREATED)

    print(serialized_reservation.errors)
    return Response(
        serialized_reservation.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# @csrf_protect nao consegui fazer funcionar...
def delete_reservation(request, reservation_id):
    print(reservation_id)
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
