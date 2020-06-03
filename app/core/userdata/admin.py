from django.contrib import admin
from .models import Roles, DatosUser, HabilUser, DetaRoles,Rates

# Register your models here.
# Registro del modelo de Roles:
class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links = ["RoleName"]
    list_filter = ["RoleName"]
    class Meta:
        model = Roles

admin.site.register(Roles)

#Registro del modelo de DatosUser:
class DatosUserModel(admin.ModelAdmin):
    list_display = ["nombUser"]
    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

#Registro del modelo de HabilUser:
class HabilUserModel(admin.ModelAdmin):
    list_display = ["NombHabil"]
    class Meta:
        model = HabilUser

admin.site.register(HabilUser)

#Registro del modelo de DetaRoles:
class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idUser"]
    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

#Registro del modelo de Rates:
class RatesModel(admin.ModelAdmin):
    list_display = ["idUser"]
    class Meta:
        model = Rates

admin.site.register(Rates)