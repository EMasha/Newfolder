# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *



# Register your models here.
admin.site.register(prona, LeafletGeoAdmin)
admin.site.register(biznes)
admin.site.register(status)
admin.site.register(qytet)
admin.site.register(rruget)
admin.site.register(zona)
admin.site.register(vendodhje)
admin.site.register(atributi)
admin.site.register(foto)
admin.site.register(lloji)

