from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserAccount, ActivityForm

@receiver(post_save, sender=User)
def create_UserAccount(sender, instance, created, **kwargs):
    if created:
        user_form = ActivityForm.objects.filter(Email=instance.email).first()
        newAccount, created = UserAccount.objects.get_or_create(user=instance, form=user_form)
        newAccount.save()
