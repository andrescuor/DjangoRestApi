from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
# Create your views here.

class StaffListApiView(ListAPIView):
    serializer_class = StaffSerializer
    def get_queryset(self):
        return Staff.objects.all()

class StaffCreateView(CreateAPIView):
    serializer_class = StaffSerializer


class StaffRetrieveView(RetrieveAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffDeleteView(DestroyAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffUpdateView(RetrieveUpdateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffOldestManager(ListAPIView):
    serializer_class = StaffSerializer

    def get(self, request, format=None):
        apiview = Staff.objects.filter(rol=0).order_by('birth').first()
        return Response({'message': 'El tecnico mas viejo',
                         'apiview': apiview})

