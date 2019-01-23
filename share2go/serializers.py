
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Profile,Note

# class UserSerializer(serializers.ModelSerializer):
#     email=serializers.EmailField(required=True,
#     validators=[UniqueValidator(queryset=User.objects.all())]
#     )

#     username=serializers.CharField(required=True,
#     validators=[UniqueValidator(queryset=User.objects.all())]

#     password=serializers.CharField(required=True,
#     max_length=12)

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#             validated_data['password'])
#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['username','bio','avatar']
        

class NoteSerializer(serializers.ModelSerializer):
    creator=serializers.HiddenField(default=serializers.CurrentUserDefault())
    read_only_fields=['creator']
    class Meta:
        model=Note
        fields=['receiver','note_text','creator']


    def create(self,validated_data):
        # validated_data['user'] = self.request.user
        # return super(PhotoListAPIView, self).create(validated_data)
        receiver=validated_data.get('receiver')
        creator=validated_data.get('creator')
        note_text=validated_data.get('note_text')
        
        instance=Note.objects.create(creator=creator,note_text=note_text)
        print(receiver)
        # return Notes.objects.create(**validated_data)
        return instance.receiver.add(receiver[User][id])
    