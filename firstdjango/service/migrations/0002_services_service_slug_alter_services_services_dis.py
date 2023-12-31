# Generated by Django 4.2 on 2023-05-09 13:02

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='service_icon', unique=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='services_dis',
            field=models.TextField(max_length=1000),
        ),
    ]
