from django.contrib import admin
from .models import Animal
from .models import Kind


admin.site.register(Animal)
admin.site.register(Kind)