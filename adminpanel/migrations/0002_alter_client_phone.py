# Generated by Django 3.2.9 on 2021-11-21 16:41

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]