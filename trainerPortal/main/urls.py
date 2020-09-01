from django.urls import path
from rest_framework import routers
from . import views

# Routers
router = routers.DefaultRouter()
router.register("ActivityForm", views.FormRequest, basename="Form")

# URLS
urlpatterns = router.urls