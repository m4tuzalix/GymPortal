from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import User, UserAccount, ActivityForm

@receiver(post_save, sender=User)
def create_UserAccount(sender, instance, created, **kwargs):
    if created:
        user_form = ActivityForm.objects.filter(Email=instance.email).first()
        if user_form:
            user_form.Confirmed = True
            user_form.save()
            newAccount, created = UserAccount.objects.get_or_create(user=instance, form=user_form)
            newAccount.save()
        else:
            print("Manually added user")

@receiver(pre_delete, sender=User)
def DeleteUserForm(sender, instance, **kwargs):
    user_form = ActivityForm.objects.get(Email=instance.email)
    user_form.delete()


