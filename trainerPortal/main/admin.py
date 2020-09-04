from django.contrib import admin
from .models import *

<<<<<<< HEAD
all_models = [ActivityForm, UserAccount]
for model in all_models:
    admin.site.register(model)
=======
admin.site.register(ActivityForm)
>>>>>>> c751d28095b7d6a8de76d07b84df53ee2948b8d5
