from django.contrib import admin
from .models import Animal, Kind, Comment


admin.site.register(Animal)
admin.site.register(Kind)
admin.site.register(Comment)
