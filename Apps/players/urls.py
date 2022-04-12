from django.urls import path, include
from Apps.players import views

urlpatterns = [
    # CRUD ENDPOINTS
    path('create/', views.PlayerCreateView.as_view()),
    path('list/', views.PlayerListApiView.as_view()),
    path('update/<pk>/', views.PlayerUpdateView.as_view()),
    path('delete/<pk>/', views.PlayerDeleteView.as_view()),

    # OTHER ENDPOINTS

    # Total de jugadores
    path('get-total/', views.PlayerTotal.as_view()),
    # Total de suplentes
    path('get-total-sub/', views.PlayerTotalSub.as_view()),
    # Jugador mas Joven
    path('get-youngest/', views.PlayerYoungest.as_view()),
    # Jugador mas viejo
    path('get-oldest/', views.PlayerOldest.as_view()),
    # Promedio Jugadores por equipo
    path('get-average/', views.TeamAverage.as_view()),
    # Promedio Jugadores por equipo
    path('age-avg/', views.AgeAvg.as_view()),

]
