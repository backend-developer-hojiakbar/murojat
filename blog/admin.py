from django.contrib import admin
from .models import Passport, Government, AppealType, Petition
# Register your models here.
@admin.register(Passport)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name']

@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(AppealType)
class AppealTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ['government', 'appealType']
    list_filter = ['government', 'appealType']