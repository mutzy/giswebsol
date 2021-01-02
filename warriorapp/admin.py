from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import dataimport

@admin.register(dataimport)
class dataimportAdmin(ImportExportModelAdmin):
    #list_filter = ('country','province','narrative',)

    list_display = (
        'id',
        'hour',
        'minutes',
        'period',
        'country',
        'province',
        'latitude',
        'longtitude',
        'narrative',
        )
    search_fields = ['period','country','province','narrative']