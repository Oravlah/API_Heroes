from rest_framework.viewsets import ModelViewSet
from heroes.models import Heroes
from heroes.apiheroes.serializers import HeroesSerializer




class HeroesApiViewSet(ModelViewSet):
    serializer_class = HeroesSerializer
    queryset = Heroes.objects.all()
