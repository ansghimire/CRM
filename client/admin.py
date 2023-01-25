from django.contrib import admin
from .models import Client, Note


# Register your models here.
admin.site.register(Client)
admin.site.register(Note)