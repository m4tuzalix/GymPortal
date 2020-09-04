from django.urls import path
from rest_framework import routers
from . import views

# Routers
router = routers.DefaultRouter()
<<<<<<< HEAD
router.register("activityform", views.FormRequest, basename="form")
router.register("allforms", views.UserAccountCreation, basename="allforms")
=======
router.register("ActivityForm", views.FormRequest, basename="Form")
>>>>>>> c751d28095b7d6a8de76d07b84df53ee2948b8d5

# URLS
urlpatterns = router.urls