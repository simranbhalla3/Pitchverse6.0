from django.contrib import admin
from .models import User

# Register your models here.

class Changes(admin.ModelAdmin):
	list_display = ('email','name' ,'team', 'position')
	list_filter = ('team',)
		

admin.site.register(User, Changes)
