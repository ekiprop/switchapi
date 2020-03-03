from django.shortcuts import render

from smartswitchapi.models import Switchapi
from rest_framework import viewsets
from . serializers import SwitchapiSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'switchapi': reverse('switchapi-list', request=request, format=format)
    })


class SwitchapiViewSet(viewsets.ModelViewSet):

    queryset = Switchapi.objects.all()
    serializer_class = SwitchapiSerializer

    def perform_create(self, serializer):
        serializer.save()
