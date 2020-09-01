from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .serializers import ActivityFormSerializer
from .models import ActivityForm

class FormRequest(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = ""
    serializer_class = ActivityFormSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny,]

    def create(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        return Response({"message":"GET not available"}, status=status.HTTP_201_CREATED)

            




