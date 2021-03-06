from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .serializers import ActivityFormSerializer, AccountSerializer
from .models import ActivityForm, User
from string import ascii_letters
from random import choice


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
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserAccountCreation(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = ActivityForm.objects.filter(Confirmed=False)
    serializer_class = AccountSerializer
    permission_classes = [AllowAny,]
    data = {}

    def list(self, request, format=None):
        queryset = self.get_queryset()
        serializer = ActivityFormSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            password = "1234"
            user = f"User{User.objects.count()+1}"
            self.data["user"] = f"User{User.objects.count()+1}"
            self.data["email"] = serializer.validated_data["email"]
            self.data["response"] = "User created"
            serializer.save(username=user, password=password)
            return Response(self.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            




