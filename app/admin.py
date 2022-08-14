from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

@admin.register((User))
class adminImages(admin.ModelAdmin):
    # list_filter = ('name', )
    search_fields = ['name']

