from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from django.db.models import Max

from .serializers import *
import datetime
from datetime import date
# Create your views here.

class PlayerListApiView(ListAPIView):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        return Player.objects.all()



class PlayerCreateView(CreateAPIView):
    serializer_class = PlayerSerializer


class PlayerRetrieveView(RetrieveAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerDeleteView(DestroyAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerUpdateView(RetrieveUpdateAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


# Personalizados
class PlayerTotal(APIView):
    serializer_class = PlayerSerializer

    def get(self, request, format=None):
        apiview = Player.objects.count()
        return Response({'message': 'Total Jugadores Registrados',
                         'apiview': apiview})


class PlayerTotalSub(APIView):
    serializer_class = PlayerSerializer

    def get(self, request, format=None):
        apiview = Player.objects.filter(is_starter=False).count()
        return Response({'message': 'Total Jugadores Suplentes Registrados',
                         'apiview': apiview})


class PlayerYoungest(APIView):
    serializer_class = PlayerSerializer

    def get(self, request, format=None):
        apiview = Player.objects.order_by('birth').last()
        return Response({'message': 'Jugador mas Joven',
                         'apiview': str(apiview)})


class PlayerOldest(APIView):
    serializer_class = PlayerSerializer

    def get(self, request, format=None):
        apiview = Player.objects.order_by('birth').first()
        return Response({'message': 'Jugador con mas viejo',
                         'apiview': str(apiview)})


class TeamAverage(APIView):
    serializer_class = PlayerSerializer

    def get(self, request, format=None):
        apiview = Team.objects.annotate(numberteam=Count('player'))
        team_players = []
        for i in apiview:
            team_players.append(i.numberteam)
        average = sum(team_players)/len(team_players)

        return Response({'message': 'Promedio jugadores por equipo',
                         'average': int(average)})


class AgeAvg(APIView):
    serializer_class = PlayerSerializer

    def get(self, request, format=None):
        #apiview = Player.objects.annotate(dateofbirth=Max('birth'))
        apiview = Player.objects.all()
        team_players = []
        '''for i in apiview:
            team_players.append(i.dateofbirt)
        today= date.today()
        '''
        return Response({'message': 'Promedio de edad',
                         'Biggest Team': apiview})



