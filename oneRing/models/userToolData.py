from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
mode = (('y','Yes'),
        ('n','No')
       )
class userToolData(models.Model):
    user   = models.OneToOneField(User,
                                  on_delete=models.CASCADE)

    cardID = models.CharField(max_length = 30,
                              blank      = True)

    banned = models.CharField(default    = 'n',
                              choices    = mode,
                              max_length = 2
                              )

    @property
    def isValid(self):
        if self.banned == 'y':
            return False

        else:
            return True

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userToolData.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.usertooldata.save()