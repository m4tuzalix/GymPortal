from rest_framework.serializers import ModelSerializer
from .models import ActivityForm

class ActivityFormSerializer(ModelSerializer):
    class Meta:
        model = ActivityForm
        fields = ["Age", "Activity", "Email", "Additional"]

