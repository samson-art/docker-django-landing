from django.contrib import admin
from .models import Decor

@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    pass
