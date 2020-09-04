<<<<<<< HEAD
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
        fields = ["email", "password"]
    
=======
from rest_framework.serializers import ModelSerializer
from .models import ActivityForm

class ActivityFormSerializer(ModelSerializer):
    class Meta:
        model = ActivityForm
        fields = ["Age", "Activity", "Email", "Additional"]
>>>>>>> c751d28095b7d6a8de76d07b84df53ee2948b8d5

