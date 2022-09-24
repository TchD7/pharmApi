from django.contrib import admin
from dashbord.models import Pharms,Commune,Pharms_de_garde


# Register your models here.
admin.site.register(Pharms)
admin.site.register(Commune)
admin.site.register(Pharms_de_garde)

