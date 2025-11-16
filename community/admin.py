from django.contrib import admin
from .models import Party
from .models import Constituency

# Register your models here.
admin.site.register(Party)
admin.site.register(Constituency)