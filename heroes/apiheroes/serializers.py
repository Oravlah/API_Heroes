from rest_framework import serializers
from heroes.models import Heroes



class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = ['id','nombre', 'alias', 'edad', 'poder', 'nacionalidad', 'descripcion']
        #fields = '__all__'