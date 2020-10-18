from django.contrib import admin
from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
     class meta:
         fields='__all__'
admin.site.register(Image)