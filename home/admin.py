from django.contrib import admin

# Register your models here.
from home import models

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.User, UserAdmin)

@admin.register(models.Ride)
class RideModelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Faq)
class FaqModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Policy)
class PolicyModelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Trip)
class TripModelAdmin(admin.ModelAdmin):
    pass