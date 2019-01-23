

from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('firstname','lastname','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','location','birthdate')
