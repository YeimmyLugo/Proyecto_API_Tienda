from django.contrib import admin
from .models import Cafeteria
# Register your models here.

class CafeteriaAdmin(admin.ModelAdmin):
    list_display = (
            "referencia",
            "producto",
            "marca",
            "precio",
            "image",
            "calorias",
            "fecha_vencimiento",
    )
    
admin.site.register(Cafeteria, CafeteriaAdmin)
