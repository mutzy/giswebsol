from import_export import resources
from .models import dataimport

class dataimportResource(resources.ModelResource):
    class meta:
        model = dataimport
