# Generated by Django 4.2 on 2023-05-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactquery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='usernumber',
            field=models.IntegerField(),
        ),
    ]