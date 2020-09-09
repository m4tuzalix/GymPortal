from rest_framework import serializers
from .models import ActivityForm
from django.contrib.auth.models import User


class ActivityFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityForm
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]
    

