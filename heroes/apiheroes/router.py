from rest_framework.routers import DefaultRouter
from heroes.apiheroes.views import HeroesApiViewSet




router_heroes = DefaultRouter()

router_heroes.register(prefix='heroes', basename='heroes', viewset=HeroesApiViewSet)