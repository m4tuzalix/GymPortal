from django.urls import path
from rest_framework import routers
from . import views

# Routers
router = routers.DefaultRouter()
router.register("activityform", views.FormRequest, basename="form")
router.register("allforms", views.UserAccountCreation, basename="allforms")

# URLS
urlpatterns = router.urls