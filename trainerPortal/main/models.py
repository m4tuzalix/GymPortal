from django.db import models
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

    def __str__(self):
        return f'{self.Email} request'
