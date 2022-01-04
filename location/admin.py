from django.contrib import admin
from .models import Cargo
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


