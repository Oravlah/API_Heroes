from django.contrib import admin
from heroes.models import Heroes




@admin.register(Heroes)
class HeroesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alias', 'edad', 'poder', 'nacionalidad', 'descripcion')
    