from rest_framework import serializers
from .models import Cafeteria

class CafateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeteria
        fields = (
            "id",
            "referencia",
            "producto",
            "marca",
            "precio",
            "image",
            "calorias",
            "fecha_vencimiento",
        )
        