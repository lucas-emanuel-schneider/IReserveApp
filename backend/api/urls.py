from django.urls import path
from .views import (
                    get_reservations,
                    get_stations,
                    post_reservation,
                    get_csrf_token,
                    login_user,
                    logout_user)

urlpatterns = [
    path('get-csrf-token', get_csrf_token, name='get-csrf-token'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path("reservations", get_reservations, name="reservations"),
    path("reservations/create", post_reservation, name="create_reservation"),
    path("stations", get_stations, name="stations"),
]
