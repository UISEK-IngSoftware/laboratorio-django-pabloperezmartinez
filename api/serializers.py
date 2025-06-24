from rest_framework import serializers
import base64
from django.core.files.base import ContentFile
from pokedex.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Pokemon
        fields = '__all__'
    
    def validate_picture(self, value):
        if value:
            try:
                # Decodificar base64
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'temp.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("Invalid base64 image")
        return None