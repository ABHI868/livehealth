

from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver




# from django.db.models import Q

# class EmailAuthenticate(object):

#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(Q(email=username) | Q(username=username))
#         except User.DoesNotExist:
#             return None
#         except MultipleObjectsReturned:
#             return User.objects.filter(email=username).order_by('id').first()

#         if user.check_password(password):
#             return user
#         return None

#     def get_user(seld,user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class Note(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    note_text=models.TextField(max_length=1000)
    receiver=models.ManyToManyField(User,related_name='note_receiver',blank=True)

    def __str__(self):
        return self.creator



# @receiver(post_save,sender=User)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)  

# @receiver(post_save,sender=User)
# def save_user(sender,instance,**kwargs):
#     instance.save()





