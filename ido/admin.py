from django.contrib import admin
from .models import Survey

class customAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'major', 'enter_time']


admin.site.register(Survey, customAdmin)

# Register your models here.
