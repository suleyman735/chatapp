from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email',]
    # list_filter = ['lang']

admin.site.register(User,UserAdmin)