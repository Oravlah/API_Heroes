from rest_framework.viewsets import ModelViewSet
from heroes.models import Heroes
from heroes.apiheroes.serializers import HeroesSerializer
from heroes.apiheroes.permissions import IsAdminOrReadOnly




class HeroesApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = HeroesSerializer
    queryset = Heroes.objects.all()
