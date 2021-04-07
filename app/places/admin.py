from django.contrib import admin

from places.models import Road, StateDistrict, Place, County

admin.site.register(Road)
admin.site.register(Place)
admin.site.register(StateDistrict)
admin.site.register(County)
