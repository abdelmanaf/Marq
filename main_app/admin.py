from django.contrib import admin
from .models import Event, Todo, Importance_levels

# Register your models here.
admin.site.register(Todo)
admin.site.register(Importance_levels)
admin.site.register(Event)