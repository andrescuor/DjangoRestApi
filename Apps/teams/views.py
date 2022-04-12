from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .serializers import *
# Create your views here.

class HelloApiView(APIView):
    '''APIView de prueba'''

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        '''Retornar lista de caracteristicas'''

        apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete',
            'es similar a una vista de DJANGO',
            'Mapea manualmente a los URLs'
        ]

        return Response({'message': 'Hello',
                         'apiview': apiview})

    def post(self, request):
        '''Crea un msn con nuestro nombre'''
        serializer = self.serializer_class(data=request.data) #manera estandar para obtener el view

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''Actualiza el objeto'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class TeamListApiView(ListAPIView):
    serializer_class = TeamSerializer
    def get_queryset(self):
        return Team.objects.all()


class TeamCreateView(CreateAPIView):
    serializer_class = TeamSerializer


class TeamRetrieveView(RetrieveAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamDeleteView(DestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamUpdateView(RetrieveUpdateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamTotal(APIView):
    serializer_class = TeamSerializer

    def get(self, request, format=None):
        apiview = Team.objects.count()
        return Response({'message': 'Esta es la cantidad de equipo registrados',
                         'apiview': str(apiview)})
