from django.db import models

class query(models.Model):
    username=models.CharField(max_length=60)
    usernumber=models.IntegerField()

# Create your models here.
