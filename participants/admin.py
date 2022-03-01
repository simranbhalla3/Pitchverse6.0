from django.contrib import admin
from .models import PreEvent

# Register your models here.
class PreEventAdmin(admin.ModelAdmin):
    list_display=('Team_name','Member1_name','Member2_name')


admin.site.register(PreEvent,PreEventAdmin)    