from django.contrib import admin
from .models import Survey,graph_Survey

class customAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'major', 'enter_time']
    list_filter = ('name', 'major')
    search_fields = ['name', 'major','phone_num']




admin.site.register(Survey, customAdmin)
admin.site.register(graph_Survey)
# Register your models here.
