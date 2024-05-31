from django.contrib import admin
from zip_codes_mx.models import State, City, PostalCode, Settlement

# Model Registration

admin.site.register(State)
admin.site.register(City)
admin.site.register(PostalCode)
admin.site.register(Settlement)
