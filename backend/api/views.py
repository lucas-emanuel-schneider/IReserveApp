from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import WorkStationSerializer
from .models import WorkStation
from django.http import JsonResponse
import json
from rest_framework.permissions import IsAuthenticated
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

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
                return JsonResponse({'X-CSRFToken': get_token(request)})
            else:
                return JsonResponse({'error': 'Invalid email or password'})
        else:
            return JsonResponse({'error': 'Missing email or password'})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_stations(request):
    stations = WorkStation.objects.all()
    serialized_stations = WorkStationSerializer(stations, many=True)
    return Response(serialized_stations.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def create_user(request):
#     serialized_user = UserSerializer(data=request.data)
#     if serialized_user.is_valid():
#         serialized_user.save()
#         token = get_token(request)
#         return Response({'X-CSRFToken': token}, status=status.HTTP_201_CREATED)
#     return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        request.session.flush()
        return Response(status=status.HTTP_200_OK)


# @api_view(['GET'])
# def task_list(request):
#     tasks = Task.objects.all()
#     if not tasks:
#         return Response({'message': 'No tasks found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     serialized_tasks = TaskSerializer(tasks, many=True)
#     return Response(serialized_tasks.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def task_detail(request, pk):
#     task = Task.objects.get(id=pk)
#     serialized_task = TaskSerializer(task)
#     return Response(serialized_task.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def task_create(request):
#     serialized_task = TaskSerializer(data=request.data)
#     if serialized_task.is_valid():
#         serialized_task.save()
#         return Response(serialized_task.data, status=status.HTTP_201_CREATED)
#     return Response(serialized_task.errors, status=status.HTTP_400_BAD_REQUEST)
