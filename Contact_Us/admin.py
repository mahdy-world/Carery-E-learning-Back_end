from django.contrib import admin
from .models import Contact
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_filter = ['name', 'subject','created_on','active']
    list_display = ['name', 'email', 'subject','active','created_on']
    search_fields = ['name', 'message','email','subject']
admin.site.register(Contact,PostAdmin)


