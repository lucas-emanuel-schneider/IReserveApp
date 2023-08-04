from django.urls import path
from .views import (
                    get_reservations,
                    get_stations,
                    post_reservation,
                    delete_reservation,
                    get_csrf_token,
                    login_user,
                    logout_user)

urlpatterns = [
    path('get-csrf-token', get_csrf_token, name='get-csrf-token'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path("reservations/<int:user_id>", get_reservations, name="reservations"),  ## modificado para funcionar pela URL pq o token ta dando ruim
    path("reservations/create", post_reservation, name="create-reservation"),
    path(
        "reservations/delete/<int:reservation_id>",
        delete_reservation, name="delete-reservation"),
    path("stations", get_stations, name="stations"),
]
