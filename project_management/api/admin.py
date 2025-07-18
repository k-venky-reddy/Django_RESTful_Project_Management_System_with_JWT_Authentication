# Registers Clients , Projects in Django admin Dashboard
from django.contrib import admin
from .models import Client, Project

admin.site.register(Client)
admin.site.register(Project)
