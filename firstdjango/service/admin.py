from django.contrib import admin
# Register your models here.
from service.models import Services
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','services_dis')

admin.site.register(Services,ServiceAdmin)
 