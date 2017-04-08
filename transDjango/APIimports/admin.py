from django.contrib import admin
from .models import Feature
from daterange_filter.filter import DateRangeFilter

# Register your models here.




class FeatureAdmin(admin.ModelAdmin):
    # change_list_filter_template = "admin/filter_listing.html"
    list_filter = ('source_name', 'id')


admin.site.register(Feature, FeatureAdmin)
