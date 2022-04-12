from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import Todo

# Register your models here.

admin.site.register(Todo)


class FilterTokenAdmin(admin.ModelAdmin):
    search_fields = ['user__email', 'user__username']


admin.site.register(Token, FilterTokenAdmin)
