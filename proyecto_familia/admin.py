from django.contrib import admin
from .models import Familia

# Register your models here.

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'fecha_cumpleaños', 'parentesco')

admin.site.register(Familia,FamiliaAdmin)