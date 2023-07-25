from django.db import models
from autoslug import AutoSlugField
class Services(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_image=models.FileField(upload_to="service/",max_length=300,null=True,default=None)
    services_dis=models.TextField(max_length=1000)
    service_slug=AutoSlugField(populate_from='service_icon',unique=True,null=True,default=None)

# Create your models here.
