
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Note



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id', 'username', 'first_name']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'first_name']

class NoteSerializer(serializers.ModelSerializer):
    # creator=ser ializers.HiddenField(default=serializers.CurrentUserDefault())
    creator=UserSerializer(default=serializers.CurrentUserDefault())
    receiver_details=UserSerializer(source='receiver', read_only=True, many=True)
    # read_only_fields=['creator']

    class Meta:
        model=Note
        fields='__all__'
    
    def create(self,validated_data):
        
        receiver=validated_data.get('receiver')
        
        creator=validated_data.get('creator')
        # creator=validated_data(serializers.CurrentUserDefault().usernam)
        note_title=validated_data.get('note_title')
        note_description=validated_data['note_description']
        instance=Note.objects.create(creator=creator,note_title=note_title,note_description=note_description)
        
        instance.receiver.set(receiver)
        return instance

