from django.contrib import admin
from apps.agenda.models import Contacto
# Register your models here.
@admin.register(Contacto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','email','numero']
    