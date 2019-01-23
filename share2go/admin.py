from django.contrib import admin

# Register your models here.
from .models import Profile,Note

admin.site.register(Profile)

admin.site.register(Note)