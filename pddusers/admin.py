from django.contrib import admin

# Register your models here.
from pddusers.models import UserInfo

admin.site.register(UserInfo)
