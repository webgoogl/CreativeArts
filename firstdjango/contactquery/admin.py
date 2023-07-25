from django.contrib import admin

from contactquery.models import query

class queryAdmin(admin.ModelAdmin):
    list_display=('username','usernumber')

admin.site.register(query,queryAdmin)
 
# Register your models here.
