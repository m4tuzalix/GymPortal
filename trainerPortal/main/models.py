from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

=======
>>>>>>> c751d28095b7d6a8de76d07b84df53ee2948b8d5
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
<<<<<<< HEAD

=======
>>>>>>> c751d28095b7d6a8de76d07b84df53ee2948b8d5
class ActivityForm(models.Model):
    Age = models.CharField(choices=Age_Category, max_length=2)
    Activity = models.CharField(choices=Sport_Activity, max_length=1)
    Email = models.EmailField(unique=True, db_index=True)
    Additional = models.TextField(max_length=500)

<<<<<<< HEAD
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(ActivityForm, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} account'
=======
    def __str__(self):
        return f'{self.Email} request'
>>>>>>> c751d28095b7d6a8de76d07b84df53ee2948b8d5
