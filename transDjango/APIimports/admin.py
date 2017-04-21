from django.contrib import admin
from .models import Feature

# Register your models here.


class FeatureAdmin(admin.ModelAdmin):
    list_filter = ['source_name']
    search_fields = ['id']


admin.site.register(Feature, FeatureAdmin)

