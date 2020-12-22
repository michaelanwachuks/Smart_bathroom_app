from django.contrib import admin
from .models import bathroom
from .models import Regusers

admin.site.register(bathroom)
admin.site.register(Regusers)

#create the header
admin.site.site_header="Smart bathroom updater"
 

# Register your models here.
