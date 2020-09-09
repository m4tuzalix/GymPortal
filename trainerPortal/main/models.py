from django.db import models
from django.contrib.auth.models import User

Age_Category = {
    ("T","15-18"),
    ("Y","18-21"),
    ("A","21-40"),
    ("MA","40-60"),
    ("O","30+")
}
Sport_Activity = {
    ("L", "LOW"),
    ("M", "MIDDLE"),
    ("H", "HIGH")
}
class ActivityForm(models.Model):
    Age = models.CharField(choices=Age_Category, max_length=2)
    Activity = models.CharField(choices=Sport_Activity, max_length=1)
    Email = models.EmailField(unique=True, db_index=True)
    Additional = models.TextField(max_length=500)
    Confirmed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.Email}'

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    form = models.ForeignKey(ActivityForm, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.user.email} account'
