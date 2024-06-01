from django.contrib import admin
from .models import MatkiPszczele, TypUla, PosiadaneUle, Lokalizacja

admin.site.register(MatkiPszczele)
admin.site.register(TypUla)
admin.site.register(Lokalizacja)
admin.site.register(PosiadaneUle)