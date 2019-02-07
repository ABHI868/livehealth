

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.user.username)
    

class Note(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    note_title=models.CharField(max_length=30)
    note_description=models.TextField(max_length=1000)
    note_created_date=models.DateTimeField(auto_now_add=True)
    receiver=models.ManyToManyField(User,related_name='note_receiver',blank=True)


    def __str__(self):
        return self.note_title


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile=Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)




